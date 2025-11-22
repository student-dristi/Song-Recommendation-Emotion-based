import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Use Client Credentials Flow (no user login needed) for playlist search
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = Spotify(auth_manager=auth_manager)

def search_playlist_by_genre(genre, limit=5):
    results = sp.search(q=f"genre:{genre}", type="playlist", limit=limit)
    print("Spotify search results:", results)  # DEBUG
    playlists = []
    for item in results.get('playlists', {}).get('items', []):
        if item is None:
            continue  # skip None items
        playlists.append({
            "name": item.get('name', 'Unknown'),
            "url": item.get('external_urls', {}).get('spotify', '')
        })
    return playlists
