from platform import release
import lyrics
import downloader
import getdatafromspotify
import os
import add_metadata

# Check link type
def check_link_type(link):
    if link.startswith("https://open.spotify.com/track/"):
        return "track"
    elif link.startswith("https://open.spotify.com/album/"):
        return "album"
    elif link.startswith("https://open.spotify.com/playlist/"):
        return "playlist"
    else:
        return "invalid"

if __name__ == "__main__":
    # Get link from user
    link = input("Enter link: ")
    link_type = check_link_type(link)
    audiofile = ""
    # Download lyrics
    if link_type == "track":
        song_data = getdatafromspotify.get_song_data(getdatafromspotify.get_song_uri_from_link(link))
        artist = getdatafromspotify.get_song_artist(song_data)
        title = getdatafromspotify.get_song_title(song_data)
        album = getdatafromspotify.get_song_album(song_data)
        release_date = getdatafromspotify.get_song_release_date(song_data)
        lyrics_text = lyrics.get_lyrics(artist, title)
        album_cover = getdatafromspotify.get_song_album_cover(song_data)
        track_number = getdatafromspotify.get_song_track_number(song_data)
        try:
            downloader.download(artist, title)
        except:
            print("[error] Could not download {}".format(artist + " - " + title))

        # Download album cover
        try:
            downloader.download_from_link(album_cover, title + ".album_cover.jpg")
        except:
            print("[error] Could not download album cover")
        # Add metadata
        add_metadata.add_song_metadata(artist + " - " + title, artist, title, album, release_date, lyrics_text, title + ".album_cover.jpg", track_number)
    elif link_type == "album":
        song_uris = getdatafromspotify.get_album_songs(link)
        for song_uri in song_uris:
            song_data = getdatafromspotify.get_song_data(song_uri)
            artist = getdatafromspotify.get_song_artist(song_data)
            title = getdatafromspotify.get_song_title(song_data)
            album = getdatafromspotify.get_song_album(song_data)
            release_date = getdatafromspotify.get_song_release_date(song_data)
            lyrics_text = lyrics.get_lyrics(artist, title)
            album_cover = getdatafromspotify.get_song_album_cover(song_data)
            track_number = getdatafromspotify.get_song_track_number(song_data)
            try:
                downloader.download(artist, title)
            except:
                print("[error] Could not download {}".format(artist + " - " + title))
                continue

            # Download album cover
            try:
                downloader.download_from_link(album_cover, title + ".album_cover.jpg")
            except:
                print("[error] Could not download album cover")
                continue
            # Add metadata
            add_metadata.add_song_metadata(artist + " - " + title, artist, title, album, release_date, lyrics_text, title + ".album_cover.jpg", track_number)
    elif link_type == "playlist":
        song_uris = getdatafromspotify.get_playlist_songs(link)
        for song_uri in song_uris:
            song_data = getdatafromspotify.get_song_data(song_uri)
            artist = getdatafromspotify.get_song_artist(song_data)
            title = getdatafromspotify.get_song_title(song_data)
            album = getdatafromspotify.get_song_album(song_data)
            release_date = getdatafromspotify.get_song_release_date(song_data)
            lyrics_text = lyrics.get_lyrics(artist, title)
            album_cover = getdatafromspotify.get_song_album_cover(song_data)
            track_number = getdatafromspotify.get_song_track_number(song_data)
            try:
                downloader.download(artist, title)
            except:
                print("[error] Could not download {}".format(artist + " - " + title))
                continue

            # Download album cover
            try:
                downloader.download_from_link(album_cover, title + ".album_cover.jpg")
            except:
                print("[error] Could not download album cover")
                continue
            # Add metadata
            add_metadata.add_song_metadata(artist + " - " + title, artist, title, album, release_date, lyrics_text, title + ".album_cover.jpg", track_number)
    else:
        print("[error] Invalid link")