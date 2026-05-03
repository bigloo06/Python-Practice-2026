import sounddevice as sd
from scipy.io.wavfile import write

def rec(duration=5, name='Recording.wav'): # method which can be given duration and name, if not it defaults to 5 seconds and a simple name

    freq = 44100 # declaring the sampling frequency of the audio (usualy 44100)

    print(f'Recording for {duration} seconds')
    recording = sd.rec(int(duration * freq), # we use the sounddevice library's function rec (used for recording), the first parameter is the frames: the frame of 1 sec * duration
                    samplerate=freq, channels=2) # the second and third parameters are the samplerate and number of audio channels (either 1 or 2)

    sd.wait() # this records the audio for the given number of seconds

    write(name, freq, recording) # write is a method from scipy.io.wavfile, it writes a wave file with the given name and frequency

if __name__ == '__main__':
    rec()