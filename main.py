from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/signals")
def get_signals():
    sheet_url = "https://docs.google.com/spreadsheets/d/1JnKvJ5A0O6MBBqY8fi4MWRa5MDwN641Q6hVdCb4jsM/export?format=csv"
    try:
        df = pd.read_csv(sheet_url)
        signals = df.to_dict(orient="records")
        return {"status": "success", "data": signals}
    except Exception as e:
        return {"status": "error", "message": str(e)}
