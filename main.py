from fastapi import FastAPI
from routes.sim_routes import sim_api_router


app = FastAPI()

app.include_router(sim_api_router)