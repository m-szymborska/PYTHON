import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

date = input("Which year do you want to travel to? Date format YYYY-MM-DD")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
music_html = response.text

soup = BeautifulSoup(music_html, "html.parser")

song_title = soup.select("li ul li h3")
song_t = [song.getText().strip() for song in song_title]


client_id = '6620336d8b2d4117ad3b5df77b7f7696'
client_secret = '2e21d8ca222d4f3684f46d95a7d84fdf'

# # Initialize the Spotipy client with your credentials
# auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(auth_manager=auth_manager)


# Initialize the Spotipy client with OAuth authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                               redirect_uri='https://example.com/', scope='playlist-modify-private'))





# Now you can use `sp` to interact with the Spotify Web API

song_uris = []  # To store the Spotify URIs

for song_name in song_t:
    results = sp.search(q=f"track:{song_name}", type='track', limit=1)  # Search for the song

    if results['tracks']['items']:
        # Get the URI of the first result (assuming it's the closest match)
        track_uri = results['tracks']['items'][0]['uri']
        song_uris.append(track_uri)
    else:
        # Handle cases where the song couldn't be found
        print(f"Song '{song_name}' not found on Spotify.")

# Now, `spotify_uris` contains the Spotify URIs for the songs in your list
print(song_uris)

# # Create a playlist
user_id = 'ztmnu14wz4v40b7cysz4w46ks'
playlist_name = 'PYTHON5'
playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description='My new playlist description')


print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# Playlist creation and song addition complete
print(f"Playlist '{playlist_name}' created and songs added to it.")