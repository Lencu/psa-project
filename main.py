import wave
import pyaudio
from array import array

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
FILE_NAME = "RECORDING.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=chunk)

print("**** started recording")

frames = []

for i in range(0, int(44100 / chunk * RECORD_SECONDS)):
    data = stream.read(chunk,
                       exception_on_overflow=False)      # data is read from stream
    data_chunk = array('h', data)                        # array of integers (signed short)
    vol = max(data_chunk)                                # vol is maximum value of data_chunk
    if (vol >= 500):                                     # 500 not normalized audio THRESHOLD
        print("Now I can hear you!")
        frames.append(data)                              # append non-empty frame to data
    else:
        print("Can you speak louder?")                   # if I can't hear you, I will not record you!
    print("\n")

print("**** recording done")

stream.stop_stream()
stream.close()
p.terminate()

wavfile = wave.open(FILE_NAME, 'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(p.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))                    # append frames recorded to file
wavfile.close()
