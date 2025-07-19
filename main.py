from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import csv
import io

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "OK", "message": "Welcome to CoinGlass Signal API"}

@app.get("/signals")
def get_signals():
    # Google Sheets CSV export URL (Make sure the sheet is shared as "Anyone with the link")
    sheet_url = "https://docs.google.com/spreadsheets/d/1JnKvJ5A0O6MBBqY8fi4MWRa5MDwVn64lQ6hVdCb4jsM/export?format=csv"
    
    try:
        response = requests.get(sheet_url)
        response.raise_for_status()
        csv_text = response.text
        reader = csv.DictReader(io.StringIO(csv_text))
        signals = []

        for row in reader:
            if row["Symbol"] and row["Direction"] and row["Price"]:
                signals.append({
                    "symbol": row["Symbol"].strip(),
                    "direction": row["Direction"].strip().lower(),
                    "price": float(row["Price"])
                })

        return {"status": "OK", "data": signals}

    except Exception as e:
        return {"status": "error", "message": str(e)}
