# Importing necessary libraries
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):

    # getting spotify credentials
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    # add your keys here
    client_credentials_manager = SpotifyClientCredentials(client_id = client_id  , client_secret = client_secret)

    # Initializes a Spotify client using Spotipy with a client credentials manager for API authentication
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotipy')

    playlist_link = "https://open.spotify.com/playlist/5ABHKGoOzxkaa28ttQV9sE"
    playlist_URL = playlist_link.split("/")[-1]

    # Fetch data from the spotipy
    spotipy_data = sp.playlist_tracks(playlist_URL)

    client = boto3.client('s3')

    filename = "spotipy_raw" + str(datetime.now()) + ".json"

    client.put_object( 
        Bucket = "spotify-etl-projet-fariane",
        Key = "raw_data/to_processed/" + filename,
        Body = json.dumps(spotipy_data)
    )
