from app.collector.spotify_client import SpotifyClient
from app.db.database import SessionLocal

from app.db.models import Track, ChartSnapshot
from datetime import date

def collect_data():
    session = SessionLocal()
    sp = SpotifyClient()

    countries = ["PL", "UK", "US"]
    for country in countries:
        new_albums = sp.get_new_releases(country)
        for album in new_albums:
            tracks = sp.get_album_tracks(album['id'])
            track_ids = [track['id'] for track in tracks]
            tracks_details = sp.get_tracks_details(track_ids)
            for track in tracks_details:
                session.merge(Track(spotify_id = track['id'],
                name = track['name'],
                artist = track['artists'][0]['name'],
                album = track['album']['name'],
                album_image = track['album']['images'][0]['url'],
                popularity = track['popularity'],
                duration_ms = track['duration_ms'],
                preview_url = track['preview_url'],
        ))
                session.flush()
                session.add(ChartSnapshot(track_id = track['id'],
                market = country,
                position = None,
                snapshot_date = date.today(),
                popularity = track['popularity']))

            session.commit()
    session.close()







