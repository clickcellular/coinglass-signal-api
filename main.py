import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

COINGLASS_API_KEY = "your_actual_api_key_here"

@app.get("/api/liquidations")
def get_liquidation(symbol: str = "ETH"):
    url = "https://open-api.coinglass.com/public/v2/liquidation_history"
    headers = {
        "coinglassSecret": COINGLASS_API_KEY
    }
    params = {
        "symbol": symbol,
        "interval": "15m",  # Options: 5m, 15m, 1h, etc.
        "currency": "USDT"
    }
    response = requests.get(url, headers=headers, params=params)
    return JSONResponse(content=response.json())
