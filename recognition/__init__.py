from typing import List

import speech_recognition as sr


def recognize_words(audio_file) -> List[str]:
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            words = text.split()
    except sr.UnknownValueError:
        # Handle unrecognized input
        words = []

    return words
