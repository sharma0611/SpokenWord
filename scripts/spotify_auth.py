import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configparser

def get_token():
    config = configparser.ConfigParser()
    config.read("./config.cfg")
    section = config._sections["spotify"]
    client_id = section['client_id']
    print(section)
    client_secret = section['client_secret']
    api_URL = "https://accounts.spotify.com/api/token"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    token = client_credentials_manager.get_access_token()

    with open("./token", 'w') as f:
        f.write(token)

    return token

if __name__ == "__main__":
    get_token()


