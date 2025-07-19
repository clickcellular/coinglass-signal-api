from fastapi import FastAPI
import csv
import requests
from io import StringIO

app = FastAPI()

CSV_URL = "https://docs.google.com/spreadsheets/d/1JnKvJ5A0O6MBBqY8fi4MWRa5MDwVn64lQ6hVdCb4jsM/export?format=csv"

@app.get("/")
def root():
    return {"message": "🚀 CoinGlass Signal API is live!"}

@app.get("/signals")
def get_signals():
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()
        csv_content = StringIO(response.text)
        reader = csv.DictReader(csv_content)
        top_signals = []

        for row in reader:
            if len(top_signals) >= 3:
                break
            top_signals.append({
                "coin": row.get("Coin", "").strip(),
                "direction": row.get("Direction", "").strip(),
                "confidence": row.get("Confidence", "").strip(),
                "entry": row.get("Entry", "").strip(),
                "tp1": row.get("TP1", "").strip(),
                "tp2": row.get("TP2", "").strip(),
                "sl": row.get("SL", "").strip(),
                "timeframe": row.get("Timeframe", "").strip()
            })

        return {"signals": top_signals}

    except Exception as e:
        return {"error": str(e)}
