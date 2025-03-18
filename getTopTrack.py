import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials

# Set your credentials
CLIENT_ID = "9639059537684c01bc141775ab35101c"
CLIENT_SECRET = "4c0062e7cd0d459ba94a6215034c27d0"

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
def get_artist_id(artist_url):
    artist_id = re.search(r"https:\/\/open\.spotify\.com\/artist\/(.*?)\?si=", artist_url)
    return artist_id.group(1)
def get_top_tracks_by_artist_url(artist_url, country="VN"):
    """Fetches top tracks of an artist using their Spotify ID."""
    try:
        top_tracks = sp.artist_top_tracks(get_artist_id(artist_url), country=country)
        for idx, track in enumerate(top_tracks['tracks']):
            print(f"{track['name']}")
    except Exception as e:
        print("Error:", e)



