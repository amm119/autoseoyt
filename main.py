from getTopTrack import get_top_tracks_by_artist_url
import pandas as pd

# URL of the CSV file
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQG4w_8zcaJRgTPP8JqvkH6ka9QceNb_Xy_X2Puczr4FQkK4Z_iK9suA2mbazLVjy1dUsbwrniZ-ne3/pub?gid=0&single=true&output=csv'

# Read the CSV data into a DataFrame
df = pd.read_csv(url)
spot_link = df.iloc[:,5]
for i in spot_link:
    get_top_tracks_by_artist_url(i)
