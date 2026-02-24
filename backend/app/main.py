from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.collector import scheduler
from app.api.endpoints.tracks import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    scheduler.start_scheduler()

@app.get("/")
def root():
    return {"status": "running"}

