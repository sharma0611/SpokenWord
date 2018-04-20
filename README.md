# Spoken Word

A simple voice command prompt that allows you to run scripts with voice commands.

Comes with spotify controller as an example.

## Installation

```bash
git clone https://github.com/sharma0611/SpokenWord.git
cd SpokenWord
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Setup the voice commands and calls to scripts in `commands.py`

`commands.py`:

```python
key_word = 'spot' # your version of 'hey google'

commands = {'play': './scripts/spotify_ctrl play track'}
```

## Usage

Run spoken word in a seperate terminal window or in a screen.

```bash
python listener.py
```

Now you can talk to your computer and run your scripts when you want!

For the setup above, simply say "spot", followed by your command and any additional arguments you want to supply to that command.

For example, with the spotify setup out of the box, you can say "spot, play no limit". This will play the track No Limit by G-Eazy if you have setup the spotify credentials as described below.

## Setup Spotify Controller

If you would like to use the spotify features, you need to provide a client_id and client_secret in scripts/config.cfg.

```bash
mv scripts/config.cfg.template scripts/config.cfg
```

Then add the credentials you obtain from the Spotify developer webiste. Follow the client credentials flow as described in https://beta.developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow

The AppleScript for controlling spotify is adapted from https://github.com/dronir/SpotifyControl. However, that repo is no longer valid under the new credentials flow provided by the Spotify API, so I added some python code to take care of the authorization flow and provide a token. You can find this under `scripts/spotify_auth.py`

### Don't want to use the spotify controller?

Simply, `rm -r scripts/*` and fill `commands.py` with your own script calls and keywords!
