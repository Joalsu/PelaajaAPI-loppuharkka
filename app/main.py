from fastapi import FastAPI
from routers import players, events

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)
