from google.adk.agents import Agent
import requests
import freecurrencyapi
import os

from dotenv import load_dotenv
load_dotenv()

client = freecurrencyapi.Client(os.getenv("CURRENCY_API_KEY"))

# Tools
# Current Weather Tool
def get_weather(location: str) -> dict:
    """
    Description:
        Retrieves current weather for any city using Open-Meteo APIs.

    Args:
        location (str): Name of the city (e.g., "Mumbai").

    Returns:
        dict: Contains 'status' and 'report' with weather information, or 'error_message'.
    """
    # get the specified location coordinates!
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"
    geo_res = requests.get(geo_url).json()
    results = geo_res.get("results")

    if not results:
        return {"status": "error", "error_message": f"City '{location}' not found."}

    lat = results[0]["latitude"]
    lon = results[0]["longitude"]
    city_name = results[0]["name"]

    # Fetch current weather based on the given lan and lon
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=celsius"
    )
    weather_res = requests.get(weather_url).json()
    curr_weather = weather_res.get("current_weather")

    if not curr_weather:
        return {"status": "error", "error_message": f"Weather data not found for '{city_name}'."}

    return {
        "status": "success",
        "report": f"The current weather in {city_name} is {curr_weather['temperature']}°C"
    }

# Currency Convertor Tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Converts an amount from one currency to another using FreeCurrencyAPI.

    Args:
        amount (float): Amount to convert.
        from_currency (str): 3-letter code of the source currency (e.g., "USD").
        to_currency (str): 3-letter code of the target currency (e.g., "EUR").

    Returns:
        dict: {"status": "success", "report": "…"} or {"status": "error", "error_message": "…"}
    """
    rates_data = client.latest()
    rates = rates_data["data"]

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates:
        return {"status": "error", "error_message": f"Unknown source currency: {from_currency}"}
    if to_currency not in rates:
        return {"status": "error", "error_message": f"Unknown target currency: {to_currency}"}

    converted_amount = amount / rates[from_currency] * rates[to_currency]

    return {
        "status": "success",
        "report": f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    }

# Root Agent
root_agent = Agent(
    name = "weather_agent",
    model = "gemini-2.0-flash",
    description="Agent to answer questions about current weather or convert currencies.",
    instruction=(
    "You are a smart agent that can answer weather questions or convert currencies."
    "Tools available:"
    "1. get_weather(location: str) -> dict"
    "   - Use this for weather queries."
    "2. convert_currency(amount: float, from_currency: str, to_currency: str) -> dict"
    "   - Use this for any currency conversion."
    "Important rules:"
    "- Understand the user's query naturally."
    "- If the user asks about currency, figure out the amount and both currencies on your own."
    "- Use correct 3-letter ISO currency codes when calling convert_currency."
    "- You do NOT need any manual mapping; deduce ISO codes directly from the currency names in the query."
    "- Return only the structured output from the called tool."
),
    tools=[get_weather, convert_currency]
)