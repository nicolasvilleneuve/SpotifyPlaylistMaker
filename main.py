from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy import oauth2, SpotifyOAuth

CLIENT_ID = "INSERT CLIENT ID HERE"
CLIENT_SECRET = "INSERT CLIENT SECRET HERE"
REDIRECT_URI = "INSERT REDIRECT URI HERE"
SCOPE = 'playlist-modify-private'
USERNAME = "INSERT USERNAME HERE"

destination_date = input("What year would you like to travel to? (YYYY-MM-DD) ")
year = destination_date[0:4]

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{destination_date}")
result = response.text

soup = BeautifulSoup(result, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

top_100 = []
for song in songs:
    name = song.getText()
    top_100.append(name)

sp_oauth = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE, username=USERNAME, show_dialog=True, cache_path='token.txt'))

user_id = sp_oauth.current_user()['id']

# Search for the URI's for the songs in the top 100 #
song_URIs = []
for song in top_100:
    try:
        URI = sp_oauth.search(q=f"track:{song} year:{year}", type='track', limit=1)
        id = URI['tracks']['items'][0]['uri']
        song_URIs.append(id)
    except IndexError:
        continue
print(song_URIs)

# add that song to the playlist. If song not on spotify, exception handled previously #
new_playlist = sp_oauth.user_playlist_create(user=user_id, name=f"{destination_date} Billboard 100", public=False, collaborative=False, description="")


playlist_id = new_playlist["id"]


sp_oauth.playlist_add_items(playlist_id=playlist_id, items=song_URIs)

