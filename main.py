from fastapi import FastAPI
from routes.card_routes import card_api_router


app = FastAPI()

app.include_router(card_api_router)