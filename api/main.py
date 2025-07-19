from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(content={"message": "🚀 CoinGlass Signal API is live!"})

@app.get("/ping")
async def ping():
    return JSONResponse(content={"status": "OK", "message": "Ping successful"})
