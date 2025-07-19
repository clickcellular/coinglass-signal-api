from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK", "message": "Welcome to CoinGlass Signal API"}

@app.get("/signals")
def get_signals():
    # TEMP example return to test
    return {"status": "OK", "data": [{"symbol": "SCR", "direction": "long", "price": 0.3359}]}
