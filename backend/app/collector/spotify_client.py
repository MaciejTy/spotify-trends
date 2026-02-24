from app.config import settings
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyClient:
    def __init__(self):
        self.sp =  spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=settings.spotify_client_id,
        client_secret=settings.spotify_client_secret))

    def get_popular_tracks(self, market, limit=50):
        seen = set()
        tracks = []
        for query in ['year:2026', 'year:2025', 'genre:pop', 'genre:hip-hop', 'genre:rock']:
            results = self.sp.search(q=query, type='track', market=market, limit=limit)
            for t in results['tracks']['items']:
                if t['id'] not in seen:
                    seen.add(t['id'])
                    tracks.append(t)
        tracks.sort(key=lambda t: t['popularity'], reverse=True)
        return tracks[:limit]
