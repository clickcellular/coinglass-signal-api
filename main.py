from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CoinGlass API is working!"}

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COINGLASS_API_KEY = os.environ.get("COINGLASS_API_KEY")

@app.get("/api/liquidations")
def get_liquidations():
    url = "https://open-api.coinglass.com/public/v2/liquidation"
    headers = {
        "accept": "application/json",
        "coinglassSecret": COINGLASS_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
