Absolutely! Here's the **final, fully formatted `README.md`** in one single copy-paste-ready block:

````markdown
# Weather & Currency Agent

A Python agent that can:  
1. Retrieve **current weather** for any city.  
2. Perform **currency conversions** (only allowed currencies, see table below).  

Built using **Google ADK**, **FreeCurrencyAPI**, and Python.

---

## Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/weather-currency-agent.git
cd weather-currency-agent
````

### 2. Create and activate a virtual environment

```bash
python -m venv google-adk
source google-adk/bin/activate   # macOS/Linux
google-adk\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install google-adk freecurrencyapi
```

### 4. Add API keys in `.env` file inside `multi_tool_agent/`

Create a file `multi_tool_agent/.env` with the following content:

```
GOOGLE_API_KEY="your-google-api-key"
GOOGLE_GENAI_USE_VERTEXAI="false"
CURRENCY_API_KEY="your-freecurrency-api-key"
```

---

## How to Get API Keys

### Google API Key

1. Go to [Google AI Studio](https://studio.google.com/).
2. Login and click **Create new API Key**.
3. Select **Basic Gemini Project**.
4. Copy the API key and paste it in `multi_tool_agent/.env`.

### FreeCurrencyAPI Key

1. Go to [FreeCurrencyAPI](https://freecurrencyapi.com/).
2. Sign up for a free account.
3. Navigate to **API Keys** in your dashboard.
4. Copy the API key and paste it in `multi_tool_agent/.env`.

---

## Usage Example

```python
from multi_tool_agent.agent import root_agent

# Weather query
print(root_agent.ask("Weather in Tokyo?"))

# Currency conversion
print(root_agent.ask("Convert 100 USD to EUR"))
```

### How to run the agent

1. Open terminal and navigate to the project root folder (`weather-currency-agent`).
2. Run the agent using:

```bash
adk web
```

3. Open the link in your browser.
4. Select `multi_tool_agent`.
5. Enter queries like:

   * `"Weather in Tokyo?"`
   * `"Convert 100 USD to EUR"`

> ⚠️ Only currencies listed in the table below are supported.

---

## Allowed Currencies

| Code | Name                   |
| ---- | ---------------------- |
| EUR  | Euro                   |
| USD  | US Dollar              |
| JPY  | Japanese Yen           |
| BGN  | Bulgarian Lev          |
| CZK  | Czech Republic Koruna  |
| DKK  | Danish Krone           |
| GBP  | British Pound Sterling |
| HUF  | Hungarian Forint       |
| PLN  | Polish Zloty           |
| RON  | Romanian Leu           |
| SEK  | Swedish Krona          |
| CHF  | Swiss Franc            |
| ISK  | Icelandic Króna        |
| NOK  | Norwegian Krone        |
| HRK  | Croatian Kuna          |
| RUB  | Russian Ruble          |
| TRY  | Turkish Lira           |
| AUD  | Australian Dollar      |
| BRL  | Brazilian Real         |
| CAD  | Canadian Dollar        |
| CNY  | Chinese Yuan           |
| HKD  | Hong Kong Dollar       |
| IDR  | Indonesian Rupiah      |
| ILS  | Israeli New Sheqel     |
| INR  | Indian Rupee           |
| KRW  | South Korean Won       |
| MXN  | Mexican Peso           |
| MYR  | Malaysian Ringgit      |
| NZD  | New Zealand Dollar     |
| PHP  | Philippine Peso        |
| SGD  | Singapore Dollar       |
| THB  | Thai Baht              |
| ZAR  | South African Rand     |

---

This is **all in one block**, fully formatted, ready to paste into your `README.md`.  

Do you want me to also create a **`requirements.txt`** for this project so installation is even easier?
```
