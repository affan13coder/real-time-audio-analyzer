# 🎧 Real-Time Audio Analyzer (Waveform + FFT)

A real-time audio signal processing project built using Python.
This system captures live microphone input and visualizes both the **waveform (time domain)** and **frequency spectrum (FFT)**.

---

## 🚀 Features

* 🎤 Live audio input from microphone
* 📊 Real-time waveform visualization
* 🎧 Real-time frequency spectrum (FFT)
* ⚡ Fast Fourier Transform (FFT) for signal analysis
* 🖥️ Interactive and dynamic graphs

---

## 🛠️ Tech Stack

* Python
* NumPy
* Matplotlib
* sounddevice

---

## 📸 Output Preview

### 🔹 Waveform (Time Domain)

Displays how the audio signal varies with time.

### 🔹 Frequency Spectrum (FFT)

Displays frequency components (pitch, harmonics) present in the audio signal.

---

## 📌 How It Works

1. Captures real-time audio input using microphone
2. Processes signal in chunks (frames)
3. Applies Fast Fourier Transform (FFT)
4. Displays:

   * Waveform (time domain)
   * Frequency spectrum (frequency domain)

---

## ▶️ How to Run

### 1. Install dependencies

pip install numpy matplotlib sounddevice

### 2. Run waveform analyzer

python main.py

### 3. Run frequency analyzer

python fft.py

---

## 📂 Project Structure

real-time-audio-analyzer/
│
├── main.py          # Live waveform analyzer
├── fft.py           # Real-time frequency analyzer
├── requirements.txt
└── README.md

---

## 🎯 Future Improvements

* Add GUI using PyQt / Tkinter
* Implement noise filtering
* Add audio recording & playback
* Convert into desktop application

---

## 💡 Key Concepts Used

* Signal Processing
* Fast Fourier Transform (FFT)
* Real-Time Data Streaming
* Data Visualization

---

## 👨‍💻 Author

Affan Ahmad
