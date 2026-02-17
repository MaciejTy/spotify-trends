from fastapi import FastAPI

from app.collector import scheduler

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    scheduler.start_scheduler()

@app.get("/")
def root():
    return {"status": "running"}

