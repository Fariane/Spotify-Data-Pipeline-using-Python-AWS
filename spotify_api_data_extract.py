# Importing necessary libraries
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):

    # Fetching Spotify credentials from environment variables
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    # Initializing Spotify client credentials manager
    client_credentials_manager = SpotifyClientCredentials(client_id = client_id  , client_secret = client_secret)

    # Instantiating Spotipy client
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotipy')

    # Spotify playlist link and extraction
    playlist_link = "https://open.spotify.com/playlist/5ABHKGoOzxkaa28ttQV9sE"
    playlist_URL = playlist_link.split("/")[-1]  # Extract playlist ID from URL
    spotipy_data = sp.playlist_tracks(playlist_URL)  # Fetch playlist data

    # Initializing AWS S3 client
    client = boto3.client('s3')

    # Generating filename with timestamp
    filename = "spotipy_raw" + str(datetime.now()) + ".json"

    # Uploading the playlist data to S3
    client.put_object( 
        Bucket = "spotify-etl-projet-fariane",
        Key = "raw_data/to_processed/" + filename,
        Body = json.dumps(spotipy_data)
    )
