import spotipy
import spotipy.util as util
import json
import lyrics
from spotipy.oauth2 import SpotifyClientCredentials

clientid = 'YOUR_CLIENT_ID'
clientsecret = 'YOUR_CLIENT_SECRET'

# Connect to Spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=clientid, client_secret=clientsecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for song
def search_song(title):
    return sp.search(q=' track:' + title, type='track')

# Get playlist song uris
def get_playlist_songs(playlist_link):
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
    return track_uris

# Get song uri from link
def get_song_uri_from_link(song_link):
    return song_link.split("/")[-1].split("?")[0]

# Get album song uris
def get_album_songs(album_link):
    album_URI = album_link.split("/")[-1].split("?")[0]
    track_uris = [x["track"]["uri"] for x in sp.album_tracks(album_URI)["items"]]
    return track_uris

# Get song data
def get_song_data(song_uri):
    song = sp.track(song_uri)
    return song

# song data to json
def song_data_to_json(song_data):
    return json.dumps(song_data, indent=4)

# writing song data to file
def write_song_data_to_file(song_data, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(song_data_to_json(song_data))

# Get songs artist
def get_song_artist(song_data):
    return song_data["artists"][0]["name"]

# Get songs title
def get_song_title(song_data):
    return song_data["name"]

# Get song genre
def get_song_genre(song_data):
    return song_data["genres"][0]

# Get song release date
def get_song_release_date(song_data):
    return song_data["album"]["release_date"]

# Get song album
def get_song_album(song_data):
    return song_data["album"]["name"]

# Get song album cover
def get_song_album_cover(song_data):
    return song_data["album"]["images"][0]["url"]

# Get song lyrics
def get_song_lyrics(song_data):
    artist = get_song_artist(song_data)
    title = get_song_title(song_data)
    return lyrics.get_lyrics(artist, title)

# Get song duration
def get_song_duration(song_data):
    return song_data["duration_ms"]

# Get track number
def get_song_track_number(song_data):
    return song_data["track_number"]
