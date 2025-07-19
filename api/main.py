from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "🚀 CoinGlass Signal API is live!"}

@app.get("/signals")
def get_signals():
    # Placeholder: Replace this with live logic from your CoinGlass signal engine
    return {"signal": "Example signal from CoinGlass API"}
