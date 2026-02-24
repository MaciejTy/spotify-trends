from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.collector import scheduler
from app.api.endpoints.tracks import router
from app.db.models import Base
from app.db.database import engine

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
    Base.metadata.create_all(bind=engine)
    scheduler.start_scheduler()
    scheduler.run_initial_collect()

@app.get("/")
def root():
    return {"status": "running"}

