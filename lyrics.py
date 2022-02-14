import os
import eyed3
from lyricsgenius import Genius

# Get song lyrics
def get_lyrics(artist, song_title):
    # Connect to Genius API
    genius = Genius('1RDxZ-BUxmKFAeolkO_lTgEiIS9H7uMAPS2Bws4OvtLphm6vSHwJSBp_WiAPxD2b')

    # Get song data
    song = genius.search_song(song_title, artist)

    if song.lyrics:
        return song.lyrics
    else:
        return "No lyrics found"

# Get all mp3s in folder and sub folders
def get_mp3s():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".mp3"):
                yield os.path.join(root, file)
    return file

def addallfolderslyricses():
    for mp3 in get_mp3s():
        # Get song data
        audiofile = eyed3.load(mp3)
        artist = audiofile.tag.artist
        song_title = audiofile.tag.title
        lyrics = get_lyrics(artist, song_title)
        
        # Write lyrics to mp3 metadata
        audiofile.tag.lyrics.set(lyrics)
        audiofile.tag.save()

        # Create folder for lyrics
        if not os.path.exists(artist):
            os.makedirs(artist)
        
        # Write lyrics to file
        with open(os.path.join(artist, song_title + ".txt"), "w", encoding="utf-8") as f:
            f.write(lyrics)

def addmusicslyrics(file_name):
    # Check if file exists
    if os.path.exists(file_name):
        audiofile = eyed3.load(file_name)
        artist = audiofile.tag.artist
        song_title = audiofile.tag.title
        lyrics = get_lyrics(artist, song_title)
        
        # Write lyrics to mp3 metadata
        audiofile.tag.lyrics.set(lyrics)
        audiofile.tag.save()
    else:
        print("File does not exist")