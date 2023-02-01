import pyttsx3
import subprocess
from datetime import datetime


engine = pyttsx3.init()

# For Windows. If for other OS check docs for library pyttsx3
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')

"""The function receives text as input and returns it to an *.ogg file"""
def textToFile(text):
    fileName = f"data\\{text[0:6]}"+"" + datetime.now().strftime("%H%M%S") + ".mp3"
    fileOutName = f"data\\{text[0:6]}" + datetime.now().strftime("%H%M%S") + ".ogg"
    
    #create *.mp3 file
    engine.save_to_file(text , f'{fileName}')
    engine.runAndWait()
    
    # use ffmpeg to change *.mp3 to *.ogg file
    subprocess.run(["ffmpeg", "-i", fileName, "-c:a", "libopus", fileOutName])
    return fileOutName
