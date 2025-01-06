# Imports
import os
import threading
import concurrent.futures
from typing import Optional, List
import pyttsx3
from gtts import gTTS
from playsound import playsound
import tempfile
import hashlib
import time
import speech_recognition as sr
import subprocess


__all__ = [
    'speak',
    'speak_async',
    'speak_fast',
    'speak_cached',
    'set_voice_properties',
    'list_voices',
    'play_audio',
    'convert_audio',
    'get_audio_duration',
    'split_audio',
    'merge_audio',
    'change_audio_volume',
    'extract_audio_from_video',
    'add_audio_to_video'
]

# Global engine instance for pyttsx3
_engine = None
_voice_properties = {
    'rate': 150,      # Speed of speech (words per minute)
    'volume': 0.9,    # Volume (0.0 to 1.0)
    'voice_id': None  # Will be set to first available voice
}

# Cache directory for speech files
CACHE_DIR = os.path.join(tempfile.gettempdir(), 'trenttools_voice_cache')
os.makedirs(CACHE_DIR, exist_ok=True)


def _get_engine():
    """Get or create the global pyttsx3 engine instance."""
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty('rate', _voice_properties['rate'])
        _engine.setProperty('volume', _voice_properties['volume'])
        
        # Set default voice if not already set
        if _voice_properties['voice_id'] is None:
            voices = _engine.getProperty('voices')
            if voices:
                _voice_properties['voice_id'] = voices[0].id
                _engine.setProperty('voice', voices[0].id)
    
    return _engine

def set_voice_properties(rate: Optional[int] = None, 
                        volume: Optional[float] = None,
                        voice_id: Optional[str] = None) -> None:
    """
    Set voice properties for speech synthesis.
    
    Args:
        rate: Speed of speech (words per minute)
        volume: Volume level (0.0 to 1.0)
        voice_id: ID of the voice to use
    """
    global _voice_properties, _engine
    
    if rate is not None:
        _voice_properties['rate'] = rate
    if volume is not None:
        _voice_properties['volume'] = volume
    if voice_id is not None:
        _voice_properties['voice_id'] = voice_id
    
    # Update engine if it exists
    if _engine is not None:
        if rate is not None:
            _engine.setProperty('rate', rate)
        if volume is not None:
            _engine.setProperty('volume', volume)
        if voice_id is not None:
            _engine.setProperty('voice', voice_id)

def list_voices() -> List[dict]:
    """List all available voices with their properties."""
    engine = _get_engine()
    voices = []
    for voice in engine.getProperty('voices'):
        voices.append({
            'id': voice.id,
            'name': voice.name,
            'languages': voice.languages,
            'gender': voice.gender,
            'age': voice.age
        })
    return voices

def speak(text, lang='en'):
    """
    Converts text to speech and plays the audio.

    Args:
        text (str): The text to convert to speech.
        lang (str, optional): The language of the text. Defaults to 'en'.
    """
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        playsound.playsound(fp.name)
        os.remove(fp.name)

async def speak_async(text, lang='en'):
    """
    Converts text to speech and plays the audio asynchronously.

    Args:
        text (str): The text to convert to speech.
        lang (str, optional): The language of the text. Defaults to 'en'.
    """
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        playsound.playsound(fp.name)
        os.remove(fp.name)

def _get_cache_path(text: str) -> str:
    """Get the cache file path for a given text."""
    text_hash = hashlib.md5(text.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f'speech_{text_hash}.mp3')

def speak_cached(text: str) -> None:
    """
    Speak text using gTTS with caching for faster repeated playback.
    This method is faster for repeated phrases and doesn't block the main thread.
    """
    cache_path = _get_cache_path(text)
    
    # Create cache file if it doesn't exist
    if not os.path.exists(cache_path):
        tts = gTTS(text=text, lang='en')
        tts.save(cache_path)
    
    # Play the cached file in a separate thread
    threading.Thread(target=playsound, args=(cache_path,), daemon=True).start()

def speak_fast(text: str) -> None:
    """
    Fastest speech method using pyttsx3 with optimized settings.
    Good for short phrases that need to be spoken quickly.
    """
    engine = _get_engine()
    current_rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)  # Faster rate for quick speech
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', current_rate)  # Restore original rate

def speech_to_text(audio_file, language='en-US'):
    """
    Converts speech in an audio file to text.

    Args:
        audio_file (str): The path to the audio file.
        language (str, optional): The language of the speech. Defaults to 'en-US'.

    Returns:
        str: The transcribed text, or None if an error occurred.
    """
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        try:
            return r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def play_audio(audio_file):
    """
    Plays an audio file.

    Args:
        audio_file (str): The path to the audio file to play.
    """
    playsound.playsound(audio_file)

def convert_audio(input_path, output_path, output_format):
    """
    Converts an audio file to a different format using ffmpeg.

    Args:
        input_path (str): The path to the input audio file.
        output_path (str): The path to the output audio file.
        output_format (str): The desired output format (e.g., 'mp3', 'wav').
    """
    try:
        subprocess.run(['ffmpeg', '-i', input_path, '-vn', '-acodec', output_format, output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting audio: {e}")

def get_audio_duration(file_path):
    """
    Gets the duration of an audio file in seconds using ffprobe.

    Args:
        file_path (str): The path to the audio file.

    Returns:
        float: The duration of the audio file in seconds, or None if an error occurred.
    """
    try:
        result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path], capture_output=True, text=True, check=True)
        return float(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error getting audio duration: {e}")
        return None

def split_audio(file_path, start_time, end_time, output_path):
    """
    Splits an audio file into a segment based on start and end times using ffmpeg.

    Args:
        file_path (str): The path to the input audio file.
        start_time (float): The start time of the segment in seconds.
        end_time (float): The end time of the segment in seconds.
        output_path (str): The path to the output audio file.
    """
    try:
        subprocess.run(['ffmpeg', '-i', file_path, '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error splitting audio: {e}")

def merge_audio(file_paths, output_path):
    """
    Merges multiple audio files into a single file using ffmpeg.

    Args:
        file_paths (list): A list of paths to the input audio files.
        output_path (str): The path to the output audio file.
    """
    try:
        # Create a text file listing the input files for ffmpeg
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            for file_path in file_paths:
                f.write(f"file '{file_path}'\n")
            temp_file_name = f.name

        # Use ffmpeg to concatenate the files
        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', temp_file_name, '-c', 'copy', output_path], check=True)

        # Clean up the temporary file
        os.remove(temp_file_name)
    except subprocess.CalledProcessError as e:
        print(f"Error merging audio: {e}")

def change_audio_volume(file_path, volume, output_path):
    """
    Changes the volume of an audio file using ffmpeg.

    Args:
        file_path (str): The path to the input audio file.
        volume (float): The desired volume level (e.g., 0.5 for 50%, 2.0 for 200%).
        output_path (str): The path to the output audio file.
    """
    try:
        subprocess.run(['ffmpeg', '-i', file_path, '-filter:a', f'volume={volume}', output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error changing audio volume: {e}")

def extract_audio_from_video(video_path, audio_path):
    """
    Extracts audio from a video file using ffmpeg.

    Args:
        video_path (str): The path to the input video file.
        audio_path (str): The path to the output audio file.
    """
    try:
        subprocess.run(['ffmpeg', '-i', video_path, '-vn', '-acodec', 'copy', audio_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio from video: {e}")

def add_audio_to_video(video_path, audio_path, output_path):
    """
    Adds audio to a video file using ffmpeg.

    Args:
        video_path (str): The path to the input video file.
        audio_path (str): The path to the input audio file.
        output_path (str): The path to the output video file.
    """
    try:
        subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c', 'copy', '-map', '0:v:0', '-map', '1:a:0', output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding audio to video: {e}")

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

def _cleanup_cache():
    """Clean up old cached speech files."""
    try:
        files = os.listdir(CACHE_DIR)
        for file in files:
            file_path = os.path.join(CACHE_DIR, file)
            # Remove files older than 24 hours
            if os.path.getmtime(file_path) < time.time() - 86400:
                os.remove(file_path)
    except:
        pass

# Clean up old cache files on module import
_cleanup_cache() 