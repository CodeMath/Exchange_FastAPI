from fastapi import FastAPI
from bithumb.exchange import *
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    getBTC = Exchange(symbol="BTC")
    data = getBTC.getCandle()

    return data

