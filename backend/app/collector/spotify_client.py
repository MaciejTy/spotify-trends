from app.config import settings
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyClient:
    def __init__(self):
        self.sp =  spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=settings.spotify_client_id,
        client_secret=settings.spotify_client_secret))

    def get_new_releases(self, country, limit=50):
        results = self.sp.new_releases(country, limit=limit)
        return results['albums']['items']

    def get_album_tracks(self, album_id):
        results = self.sp.album_tracks(album_id)
        return results['items']

    def get_tracks_details(self, track_ids):
        results = self.sp.tracks(track_ids)
        return results['tracks']
