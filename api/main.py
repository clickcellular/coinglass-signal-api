from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🚀 CoinGlass Signal API is live!"}

@app.get("/signals")
async def get_signals():
    api_key = os.getenv("COINGLASS_API_KEY")
    if not api_key:
        return JSONResponse(status_code=500, content={"error": "Missing API key."})
    
    url = "https://open-api.coinglass.com/api/pro/v1/futures/liquidation_chart"
    headers = {
        "coinglassSecret": api_key
    }
    
    params = {
        "symbol": "BTCUSDT",  # Default for now
        "interval": "5m"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return {"status": "success", "data": data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
