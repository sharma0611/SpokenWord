import os
from pocketsphinx import pocketsphinx
from sphinxbase import sphinxbase
import pyaudio
import subprocess
import simpleaudio as sa

audio_sample_rate = 16000

import speech_recognition as sr

from commands import commands, key_word

#usage
#<keyword> play track No Limit
#<keyword> stop
#<keyword> start

r = sr.Recognizer()
m = sr.Microphone()

print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)

def start_keyphrase_recognition(keyphrase_function, key_phrase):
    """ Starts a thread that is always listening for a specific key phrase. Once the
        key phrase is recognized, the thread will call the keyphrase_function. This
        function is called within the thread (a new thread is not started), so the
        key phrase detection is paused until the function returns.
    :param keyphrase_function: function that is called when the phrase is recognized
    :param key_phrase: a string for the key phrase
    """
    print("Now listening...")
    modeldir = "files/sphinx/models"

    # Create a decoder with certain model
    config = pocketsphinx.Decoder.default_config()
    # Use the mobile voice model (en-us-ptm) for performance constrained systems
    config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
    # config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
    config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
    config.set_string('-keyphrase', key_phrase)
    config.set_string('-logfn', 'files/sphinx.log')
    config.set_float('-kws_threshold', 1)

    # Start a pyaudio instance
    p = pyaudio.PyAudio()
    # Create an input stream with pyaudio
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=audio_sample_rate, input=True, frames_per_buffer=1024)
    # Start the stream
    stream.start_stream()

    # Process audio chunk by chunk. On keyword detected perform action and restart search
    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()
    # Loop forever
    while True:
        # Read 1024 samples from the buffer
        buf = stream.read(1024, exception_on_overflow=False)
        # If data in the buffer, process using the sphinx decoder
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        # If the hypothesis is not none, the key phrase was recognized
        if decoder.hyp() is not None:
            keyphrase_function()
            # Stop and reinitialize the decoder
            decoder.end_utt()
            decoder.start_utt()

wave_obj_start = sa.WaveObject.from_wave_file("sounds/your_turn.wav")

def listen_and_run_command():
    print("keyword detected")
    play_start = wave_obj_start.play()
    with m as source: audio = r.listen(source, phrase_time_limit=4)
    value = r.recognize_google(audio)
    words = value.split(" ")
    key_word_spoken = words[0]
    arguments_given = words[1:].join(" ")
    cmd = commands[key_word_spoken]
    cmd = cmd + " " + arguments_given
    print("your command is: ")
    print(cmd)
    subprocess.Popen(cmd.split())
    print("finished command")

if __name__ == "__main__":
    # Start key phrase recognition and call the "demo_function" when triggered
    start_keyphrase_recognition(listen_and_run_command, key_word)

