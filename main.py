from getTopTrack import get_top_tracks_by_artist_url
import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
# URL of the CSV file
url = os.getenv('URL_DATA')

# Read the CSV data into a DataFrame
df = pd.read_csv(url)
content_artist=df['Content']
artist_name = df['Name']
spot_link = df['Spotify']
seo_add = df['SEO tag']
# for i in spot_link:
#     get_top_tracks_by_artist_url(i)
