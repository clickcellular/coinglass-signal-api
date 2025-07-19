from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK", "message": "Welcome to CoinGlass Signal API"}

@app.get("/signals")
def get_signals():
    # Replace this with your real public CSV export link
    sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"
    
    try:
        df = pd.read_csv(sheet_url)
        signals = df.to_dict(orient="records")
        return {"status": "success", "data": signals}
    except Exception as e:
        return {"status": "error", "message": str(e)}
