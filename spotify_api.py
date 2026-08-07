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
    album_artist = format_artists(album["artists"])
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
    seen = set()
    albums = []

    for album in album_results:
        album_name = album['name']
        album_artist = format_artists(album["artists"])

        # Stops duplicate albums (ex. clean and explicit versions)
        key = (album_name.lower(), album_artist.lower())

        if key in seen:
            continue

        seen.add(key)

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

def format_artists(artists):
    names = [artist["name"] for artist in artists]
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} & {names[1]}"
    else:
        return ", ".join(names[:-1]) + f" & {names[-1]}"