from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow frontend calls (adjust origin if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or your frontend URL
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
