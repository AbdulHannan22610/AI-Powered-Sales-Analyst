# AI-Powered CSV Analyst

A Streamlit sales-analysis app for loading CSV data, viewing sales charts and summary metrics, forecasting sales with the existing Random Forest model, and asking the ALLaM 2-7B assistant questions about the loaded data.

## Features

- Load the bundled `data/sample.csv` or upload a sales CSV from the sidebar.
- Filter the dashboard and AI chat by category.
- View total sales, the top product, a sales trend, product sales, and product distribution.
- Forecast total sales from quantity, unit price, and discount using the saved scikit-learn model.
- Ask natural-language questions about the selected sales data with ALLaM 2-7B.

Sales are calculated as `quantity * unit_price * (1 - discount / 100)`.

## Requirements

- Python 3.10 or newer.
- A Groq API key with access to the ALLaM-2-7B model to use AI Chat. The application calls the hosted model using the existing `requests` dependency; it does not require a separate Groq SDK.

## Setup

Run these commands from the project directory in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create a local `.env` file from the example if one does not already exist:

```powershell
Copy-Item .env.example .env
```

Edit `.env` locally and set the API key:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
```

Do not commit `.env` or put the key in application source code. The repository's `.gitignore` excludes `.env`. The app loads this variable with `python-dotenv`. `MAX_TOKENS_PER_PROMPT` is optional and defaults to `500`.

The AI Chat uses the official Groq chat-completions endpoint with the ALLaM model ID `allam-2-7b`. The API key must be authorized for this model. The chat sends the user's question and the currently selected, category-filtered data to the hosted API; avoid uploading data that should not be sent to an external service.

## Run the app

From the project directory:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Use **Load sample data** in the sidebar or upload a CSV to begin. AI Chat requires data to be loaded and a valid API key. Without the key, the chat displays a configuration message.

## CSV format

The dashboard expects these columns:

| Column | Use |
| --- | --- |
| `date` | Sales trend chart |
| `product` | Product summary and charts |
| `category` | Category filter and category analysis |
| `quantity` | Calculate sales and make predictions |
| `unit_price` | Calculate sales and make predictions |
| `discount` | Discount percentage (0–100), used for sales and predictions |

`region` is present in the bundled sample but is not required by the current dashboard calculations. See `data/sample.csv` for an example.

## Prediction model

The app loads `models/sales_model.pkl`. If this file is missing, train the existing Random Forest model from the project directory:

```powershell
.\.venv\Scripts\python.exe ml\train_model.py
```

The training script uses `data/sample.csv` and saves the resulting model to `models/sales_model.pkl`.

## Project layout

```text
app.py                  Streamlit app and page flow
config.py               .env loading and AI model configuration
data/sample.csv         Bundled sample sales data
files/                  Additional bundled sales CSV files
ml/train_model.py       Random Forest training script
ml/predict.py           Prediction helper
models/sales_model.pkl  Saved sales prediction model
services/allam.py       ALLaM chat-completions integration
utils/                  Data preparation, charts, theme, and UI helpers
requirements.txt        Python dependencies
```
