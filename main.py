from fastapi import FastAPI
import os
import requests

app = FastAPI()

COINGLASS_API_KEY = os.environ.get("COINGLASS_API_KEY")

@app.get("/api/liquidations")
def get_liquidations(symbol: str = "BTC"):
    url = f"https://open-api.coinglass.com/api/pro/v1/futures/liquidation_chart?symbol={symbol}"
    headers = {
        "accept": "application/json",
        "coinglassSecret": COINGLASS_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
