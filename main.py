from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI()

COINGLASS_API_KEY = os.environ.get("COINGLASS_API_KEY")

@app.get("/liquidations")
def get_liquidations(symbol: str = Query("ETH")):
    url = "https://open-api.coinglass.com/public/v2/liquidation_history"
    headers = {
        "coinglassSecret": COINGLASS_API_KEY
    }
    params = {
        "symbol": symbol,
        "interval": "15m",
        "currency": "USDT"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return JSONResponse(content=response.json())
    else:
        return JSONResponse(content={
            "error": True,
            "status_code": response.status_code,
            "details": response.text
        })
