from app.collector.spotify_client import SpotifyClient
from app.db.database import SessionLocal

from app.db.models import Track, ChartSnapshot
from datetime import date

def collect_data():
    session = SessionLocal()
    sp = SpotifyClient()

    countries = ["PL", "GB", "US"]
    for country in countries:
        tracks = sp.get_popular_tracks(country)
        for i, track in enumerate(tracks):
            session.merge(Track(
                spotify_id=track['id'],
                name=track['name'],
                artist=track['artists'][0]['name'],
                album=track['album']['name'],
                album_image=track['album']['images'][0]['url'] if track['album']['images'] else None,
                popularity=track['popularity'],
                duration_ms=track['duration_ms'],
                preview_url=track.get('preview_url'),
            ))
            session.flush()
            session.merge(ChartSnapshot(
                track_id=track['id'],
                market=country,
                position=i + 1,
                snapshot_date=date.today(),
                popularity=track['popularity'],
            ))
        session.commit()
    session.close()







