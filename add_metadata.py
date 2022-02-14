import eyed3
import os

# Add song metadata
def add_song_metadata(file_name, artist, title, album, release_date, lyrics_text, album_cover, track_number):
    # Debug
    print("[info] Adding metadata to {}".format(file_name))
    os.system("ffmpeg -i \"{}\" \"{}\"".format(file_name, file_name + ".mp3"))
    os.remove(file_name)

    # Add metadata
    audiofile = eyed3.load(r"{}.mp3".format(file_name))
    audiofile.tag.artist = artist
    audiofile.tag.title = title
    audiofile.tag.album = album
    audiofile.tag.release_date = release_date
    audiofile.tag.lyrics.set(lyrics_text)
    audiofile.tag.track_num = track_number
    audiofile.tag.album_cover_image_data = open(r"{}".format(album_cover), "rb").read()
    audiofile.tag.save()

    #delete album cover
    os.remove(album_cover)