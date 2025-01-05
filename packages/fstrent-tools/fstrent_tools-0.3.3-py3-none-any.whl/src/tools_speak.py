import pyttsx3
import concurrent.futures

__all__ = [
    'speak',
    'speak_async'
]

def speak(tempmessage):
    print(f'speaking : {tempmessage}...')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # changing index changes voices but only 0 and 1 are working here
    engine.setProperty('rate', 120)  # 120 words per minute
    engine.setProperty('volume', 0.9)
    engine.say(tempmessage)
    engine.runAndWait()

def speak_async(tempmessage):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(speak, tempmessage)
        return future

