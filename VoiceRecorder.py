import sounddevice as sd
from scipy.io.wavfile import write

def recTimeName(duration, name): # method which is given both the duration of recording and the file name

    freq = 44100 # declaring the sampling frequency of the audio (usualy 44100)

    recording = sd.rec(int(duration * freq), # we use the sounddevice library's function rec (used for recording), the first parameter is the frames: the frame of 1 sec * duration
                    samplerate=freq, channels=2) # the second and third parameters are the samplerate and number of audio channels (either 1 or 2)

    sd.wait() # this records the audio for the given number of seconds

    write(name, freq, recording) # write is a method from scipy.io.wavfile, it writes a wave file with the given name and frequency

def recTime(duration): #method which is given only the duration and uses a default name
    freq = 44100 # declaring the sampling frequency of the audio (usualy 44100)

    recording = sd.rec(int(duration * freq), # we use the sounddevice library's function rec (used for recording), the first parameter is the frames: the frame of 1 sec * duration
                    samplerate=freq, channels=2) # the second and third parameters are the samplerate and number of audio channels (either 1 or 2)

    sd.wait() # this records the audio for the given number of seconds

    write("recording.wav", freq, recording)

def rec(): # method which uses a standard duration of 5 seconds and a default name
    freq = 44100 # declaring the sampling frequency of the audio (usualy 44100)
    duration = 5
    recording = sd.rec(int(duration * freq), # we use the sounddevice library's function rec (used for recording), the first parameter is the frames: the frame of 1 sec * duration
                    samplerate=freq, channels=2) # the second and third parameters are the samplerate and number of audio channels (either 1 or 2)

    sd.wait() # this records the audio for the given number of seconds

    write("recording.wav", freq, recording)