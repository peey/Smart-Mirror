import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import traceback
from server import sendToClient

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("file.mp3")
        song = AudioSegment.from_mp3("file.mp3")
        # sendToClient(text)
        play(song)
        os.remove("file.mp3")
    except Exception as e:
        print(e)
        traceback.print_exc()
        sendToClient(text)
        return
