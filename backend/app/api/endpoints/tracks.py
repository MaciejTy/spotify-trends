from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.db.models import Track, ChartSnapshot


router = APIRouter()

@router.get("/tracks")
def get_tracks(market: str, db: Session = Depends(get_db)):
    return db.query(Track).join(ChartSnapshot, Track.spotify_id == ChartSnapshot.track_id).filter(
        ChartSnapshot.market == market).order_by(Track.popularity.desc()).all()

@router.get("/tracks/{spotify_id}/history")
def get_snapshot_history(spotify_id: str, db: Session = Depends(get_db)):
    return db.query(ChartSnapshot).filter(ChartSnapshot.track_id == spotify_id).order_by(ChartSnapshot.snapshot_date).all()

@router.get("/markets")
def get_markets(db: Session = Depends(get_db)):
    results = db.query(ChartSnapshot.market).distinct().all()
    return [r[0] for r in results]