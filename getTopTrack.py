import spotipy
import re
import os
from dotenv import load_dotenv, dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
# Set your credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

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



