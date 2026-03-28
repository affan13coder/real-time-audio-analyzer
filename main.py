import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

fs = 44100
block_size = 1024

# Create plot
fig, ax = plt.subplots()
x = np.arange(0, block_size)
line, = ax.plot(x, np.zeros(block_size))

ax.set_ylim(-1, 1)
ax.set_title("Live Audio Waveform")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

def update_plot(indata):
    line.set_ydata(indata[:, 0])
    plt.pause(0.001)

print("🎤 Speak... Close graph window to stop")

with sd.InputStream(channels=1, samplerate=fs, blocksize=block_size) as stream:
    while plt.fignum_exists(fig.number):
        data, _ = stream.read(block_size)
        update_plot(data)