from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/signals")
def get_signals():
    sheet_url = "https://docs.google.com/spreadsheets/d/your_sheet_id/export?format=csv"
    try:
        df = pd.read_csv(sheet_url)
        signals = df.to_dict(orient="records")
        return {"status": "success", "data": signals}
    except Exception as e:
        return {"status": "error", "message": str(e)}
