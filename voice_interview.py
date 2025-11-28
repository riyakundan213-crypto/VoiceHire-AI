# voice_interview.py
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

def transcribe_audio_file(file_path):
    r = sr.Recognizer()

    ext = file_path.split(".")[-1]
    wav_path = file_path

    if ext != "wav":
        sound = AudioSegment.from_file(file_path)
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        sound.export(temp.name, format="wav")
        wav_path = temp.name

    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
    except:
        text = ""

    if ext != "wav":
        try: os.remove(wav_path)
        except: pass

    return text

