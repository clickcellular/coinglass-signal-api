from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content={"message": "🚀 CoinGlass Signal API is live!"})

@app.get("/signals")
def get_signals():
    return JSONResponse(content={"signal": "Example signal from CoinGlass API"})
