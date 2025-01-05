import winsound
import time
from fstrent_colors import cp

__all__ = [
    'beep',
    'play_beep',
    'play_cash',
    'play_doh',
    'play_file',
    'play_sw_imperial_march',
    'play_sw_theme'
]

def beep_old():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def beep(reps=1):
    for _ in range(0, reps, 1):
        cp('beep()!!!', font='white', bg_color='red')
    play_beep(frequency=2500,duration=1000, reps=reps)

def play_beep(frequency=1000, duration=1000, reps=1):
    """
    Used to play a beep sound
    :param frequency: The frequency of the beep
    :type frequency: int
    :param duration: The duration of the beep
    :type duration: int
    """
    if winsound is None:
        print(f'play_beep(frequnecy={frequency}, duration={duration}, reps={reps}')
        return
    for _ in range(0, reps, 1):
        winsound.Beep(frequency, duration)

def play_sw_theme():
    """
    Used to play the Star Wars theme song
    """
    if winsound is None:
        print('Sound is off, you are missing SW Theme')
        return
    play_beep(1046, 880)
    play_beep(1567, 880)
    play_beep(1396, 55)
    play_beep(1318, 55)
    play_beep(1174, 55)
    play_beep(2093, 880)
    time.sleep(0.3)
    play_beep(1567, 600)
    play_beep(1396, 55)
    play_beep(1318, 55)
    play_beep(1174, 55)
    play_beep(2093, 880)
    time.sleep(0.3)
    play_beep(1567, 600)
    play_beep(1396, 55)
    play_beep(1318, 55)
    play_beep(1396, 55)
    play_beep(1174, 880)

def play_sw_imperial_march():
    """
    Used to play the Star Wars Imperial March song
    """
    if winsound is None:
        print('Sound is off, you are missing SW Imperial March')
        return
    play_beep(440, 500)
    play_beep(440, 500)
    play_beep(440, 500)
    play_beep(349, 375)
    play_beep(523, 150)
    play_beep(440, 600)
    play_beep(349, 375)
    play_beep(523, 150)
    play_beep(440, 1000)
    time.sleep(0.2)
    play_beep(659, 500)
    play_beep(659, 500)
    play_beep(659, 500)
    play_beep(698, 375)
    play_beep(523, 150)
    play_beep(415, 600)
    play_beep(349, 375)
    play_beep(523, 150)
    play_beep(440, 1000)

def play_file(f):
    winsound.PlaySound(f, winsound.SND_FILENAME)

def play_cash():
    print('play_cash()')
    play_file('sounds/cashreg.wav')

def play_doh():
    print('play_doh()')
    play_file('sounds/DOH!.WAV')

def play_thunder():
    print('play_thunder()')
    play_file('sounds/thunder.wav')
