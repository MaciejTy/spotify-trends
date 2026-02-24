from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.db.models import Track, ChartSnapshot


router = APIRouter()

@router.get("/tracks")
def get_tracks(market: str, db: Session = Depends(get_db)):
    return db.query(Track).join(ChartSnapshot, Track.spotify_id == ChartSnapshot.track_id).filter(
        ChartSnapshot.market == market).order_by(Track.popularity.desc()).all()
