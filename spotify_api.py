import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

load_dotenv()

spotify = spotipy.Spotify(
    auth_manager = SpotifyClientCredentials(
        client_id = os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)

def get_album(album_id):
    album = spotify.album(album_id)

    album_name = album['name']
    album_artist = album['artists'][0]['name']
    album_release_date = album['release_date']
    album_total_tracks = album['total_tracks']
    album_url = album['external_urls']['spotify']
    album_art = album['images'][0]['url']
    album_id = album['id']

    return {
        "name": album_name,
        "artist": album_artist,
        "release_date": album_release_date,
        "total_tracks": album_total_tracks,
        "url": album_url,
        "art": album_art,
        "id": album_id
    }

def search_albums(query):
    results = spotify.search(q=query, type="album", limit=10)
    album_results = results['albums']['items']
    albums = []

    for album in album_results:
        album_name = album['name']
        album_artist = album['artists'][0]['name']
        album_release_date = album['release_date']
        album_total_tracks = album['total_tracks']
        album_url = album['external_urls']['spotify']
        album_art = album['images'][0]['url']
        album_id = album['id']
        albums.append({
            "name": album_name,
            "artist": album_artist,
            "release_date": album_release_date,
            "total_tracks": album_total_tracks,
            "url": album_url,
            "art": album_art,
            "id": album_id
        })
    return albums
