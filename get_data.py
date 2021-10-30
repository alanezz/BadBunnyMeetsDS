import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist = sp.playlist('spotify:playlist:0zp1lc5cSY8TeLS7ocgsAK')

names = []
popularity_list = []
album_list = []
release_list = []
danceability_list = []
energy_list = []
key_list = []
loudness_list = []
speechiness_list = []
acousticness_list = []
tempo_list = []
duration_list = []
instrumental_list = []
valence_list = []

for song in playlist['tracks']['items']:
  song_id = song['track']['id']
  names.append(song['track']['name'])
  popularity_list.append(song['track']['popularity'])

  album_list.append(song['track']['album']['name'])
  release_list.append(song['track']['album']['release_date'])

  audio_features = sp.audio_features(song_id)
  danceability_list.append(audio_features[0]['danceability'])
  energy_list.append(audio_features[0]['energy'])
  key_list.append(audio_features[0]['key'])
  loudness_list.append(audio_features[0]['loudness'])
  speechiness_list.append(audio_features[0]['speechiness'])
  acousticness_list.append(audio_features[0]['acousticness'])
  tempo_list.append(audio_features[0]['tempo'])
  duration_list.append(audio_features[0]['duration_ms']/1000)
  instrumental_list.append(audio_features[0]['instrumentalness'])
  valence_list.append(audio_features[0]['valence'])

df = pd.DataFrame(
  {
    'Name': names,
    'Popularity': popularity_list,
    'Album': album_list,
    'Release': release_list,
    'Danceability': danceability_list,
    'Energy': energy_list,
    'Key': key_list,
    'Loudness': loudness_list,
    'Speechiness': speechiness_list,
    'Acousticness': acousticness_list,
    'Tempo': tempo_list,
    'Instrumentalness': instrumental_list,
    'Valence': valence_list,
    'Duration': duration_list,
  }
)

df.to_csv('bad_bunny.csv', index=False)