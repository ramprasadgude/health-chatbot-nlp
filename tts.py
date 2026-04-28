import os
import glob
from gtts import gTTS
import time

def speak_text(text, lang="en"):
    try:
        # Clean up old audio files to prevent disk space issues
        for old_file in glob.glob("static/output_*.mp3"):
            try:
                os.remove(old_file)
            except:
                pass

        filename = f"static/output_{int(time.time())}.mp3"  # 🔥 UNIQUE FILE
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        return filename
    except Exception as e:
        print("TTS Error:", e)
        return None