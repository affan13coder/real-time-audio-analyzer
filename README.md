# 🎧 Real-Time Audio Analyzer (Waveform + FFT)

A real-time audio signal processing project built using Python.  
This system captures live microphone input and visualizes both the **waveform (time domain)** and **frequency spectrum (FFT)**.

---

## 🚀 Features
- 🎤 Live audio input from microphone  
- 📊 Real-time waveform visualization  
- 🎧 Real-time frequency spectrum (FFT)  
- ⚡ Fast Fourier Transform for signal analysis  
- 🖥️ Interactive and dynamic graphs  

---

## 🛠️ Tech Stack
- Python  
- NumPy  
- Matplotlib  
- sounddevice  

---

## 📸 Output Preview

### 🔹 Waveform (Time Domain)
Shows how audio signal varies with time.

### 🔹 Frequency Spectrum (FFT)
Shows frequency components present in the audio signal.

---

## 📌 How It Works
1. Captures audio input using microphone  
2. Converts signal from time domain → frequency domain using FFT  
3. Displays both waveform and frequency spectrum in real-time  

---

## ▶️ How to Run

```bash
pip install numpy matplotlib sounddevice
python main.py   # for waveform
python fft.py    # for frequency analyzer
