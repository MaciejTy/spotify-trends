from fastapi import FastAPI

from app.collector import scheduler
from app.api.endpoints.tracks import router

app = FastAPI()
app.include_router(router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    scheduler.start_scheduler()

@app.get("/")
def root():
    return {"status": "running"}

