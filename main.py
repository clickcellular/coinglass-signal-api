from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI()

COINGLASS_API_KEY = os.environ.get("COINGLASS_API_KEY")

@app.get("/api/funding_rate")
def get_funding_rate(symbol: str = Query("BTC")):
    url = "https://open-api.coinglass.com/public/v2/funding_rate"
    headers = {
        "coinglassSecret": COINGLASS_API_KEY
    }
    params = {
        "symbol": symbol
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
