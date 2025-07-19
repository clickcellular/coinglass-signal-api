from fastapi import FastAPI
import requests
import os

app = FastAPI()

COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY")

@app.get("/api/liquidations")
def get_liquidations(symbol: str = "BTC"):
    url = f"https://open-api.coinglass.com/api/futures/liquidation_chart?symbol={symbol}"
    headers = {
        "accept": "application/json",
        "coinglassSecret": COINGLASS_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
