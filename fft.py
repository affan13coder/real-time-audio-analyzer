import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

fs = 44100
block_size = 1024

fig, ax = plt.subplots()
x = np.fft.rfftfreq(block_size, 1/fs)
line, = ax.plot(x, np.zeros(len(x)))

ax.set_xlim(0, 2000)  # focus on voice range
ax.set_ylim(0, 50)
ax.set_title("Real-Time Frequency Spectrum (FFT)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

print("🎤 Speak... Close window to stop")

with sd.InputStream(channels=1, samplerate=fs, blocksize=block_size) as stream:
    while plt.fignum_exists(fig.number):
        data, _ = stream.read(block_size)
        
        # Apply FFT
        fft_data = np.abs(np.fft.rfft(data[:, 0]))
        
        # Update graph
        line.set_ydata(fft_data)
        plt.pause(0.001)