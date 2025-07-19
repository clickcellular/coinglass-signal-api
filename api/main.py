from fastapi import FastAPI
import requests
import csv
from io import StringIO

app = FastAPI()

CSV_URL = "https://docs.google.com/spreadsheets/d/1JnKvJ5A0O6MBBqY8fi4MWRa5MDwVn64lQ6hVdCb4jsM/export?format=csv"

@app.get("/")
def root():
    return {"message": "🚀 CoinGlass Signal API is live!"}

@app.get("/signals")
def get_signals():
    try:
        response = requests.get(CSV_URL, timeout=10)
        response.raise_for_status()

        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        signals = []
        for row in reader:
            # Check that required fields are present
            if not row.get("Coin") or not row.get("Direction"):
                continue

            signals.append({
                "coin": row["Coin"].strip(),
                "direction": row["Direction"].strip(),
                "confidence": row.get("Confidence", "").strip(),
                "entry": row.get("Entry", "").strip(),
                "tp1": row.get("TP1", "").strip(),
                "tp2": row.get("TP2", "").strip(),
                "sl": row.get("SL", "").strip(),
                "timeframe": row.get("Timeframe", "").strip()
            })

            if len(signals) == 3:
                break

        return {"signals": signals}

    except Exception as e:
        return {"error": str(e)}
