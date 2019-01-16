import wave
import pyaudio
from array import array

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
FILE_NAME = "RECORDING.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=chunk)

print("* recording")

frames = []

for i in range(0, int(44100 / chunk * RECORD_SECONDS)):
    data = stream.read(chunk,
                       exception_on_overflow=False)
    data_chunk = array('h', data)
    vol = max(data_chunk)
    if (vol >= 500):
        print("something said")
        frames.append(data)
    else:
        print("nothing")
    print("\n")

print("* done")

stream.stop_stream()
stream.close()
p.terminate()

wavfile = wave.open(FILE_NAME, 'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(p.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))  # append frames recorded to file
wavfile.close()
