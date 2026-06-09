# 🤟 Smart Sign Language to Speech Translator

A wearable IoT-based Sign Language Translator that converts hand gestures into readable text and speech output in real time. This project helps bridge the communication gap between speech/hearing-impaired individuals and others using Machine Learning and Embedded Systems.

---

## 📖 Overview

The system uses **5 Flex Sensors** and an **MPU6050 motion sensor** mounted on a glove to capture finger bending and hand movement data. An **ESP32** collects the sensor readings and transmits them to a **Raspberry Pi**, where a **Random Forest Machine Learning model** predicts the corresponding gesture. The predicted gesture is displayed on a web interface and can also be converted into speech output.

---

## 🚀 Features

- Real-time sign language recognition
- Wearable smart glove design
- ESP32-based sensor data acquisition
- Raspberry Pi-based Machine Learning processing
- Random Forest Classification model
- Live web interface for gesture display
- Text-to-Speech output support
- Easy dataset collection and model retraining

---

## 🛠️ Hardware Components

- ESP32 Development Board
- Raspberry Pi
- 5 × Flex Sensors
- MPU6050 Accelerometer & Gyroscope
- Hand Glove
- Jumper Wires
- Power Supply

---

## 💻 Software & Technologies

- Python
- Arduino IDE
- ESP32
- Raspberry Pi OS
- Scikit-Learn
- Random Forest Classifier
- Pandas
- Joblib
- Serial Communication
- HTML
- CSS

---

## 📁 Project Structure

```text
sign-language-translator/
│
├── data_collect.py        # Collect gesture data from ESP32
├── train_model.py         # Train Random Forest model
├── live_predict.py        # Real-time gesture prediction
├── esp32.ino             # ESP32 sensor reading code
│
├── gesture_data.csv      # Dataset
├── gesture_model.pkl     # Trained model
│
├── templates/
│   └── index.html        # Web Interface
│
├── static/
│   └── style.css         # Frontend Styling
│
└── README.md
```

---

## ⚙️ System Architecture

```text
Flex Sensors + MPU6050
          │
          ▼
        ESP32
(Data Collection & Transmission)
          │
          ▼
     Raspberry Pi
(Machine Learning Processing)
          │
          ▼
 Random Forest Model
          │
          ▼
  Predicted Gesture
          │
    ┌─────┴─────┐
    ▼           ▼
 Web Display   Speech Output
```

---

## 🧠 Machine Learning Workflow

### 1. Data Collection

Sensor data is collected from:

- 5 Flex Sensors
- MPU6050 Accelerometer
- MPU6050 Gyroscope

The ESP32 sends the data to the Raspberry Pi where it is stored using:

```bash
python data_collect.py
```

### 2. Model Training

Train the Random Forest model using the collected dataset:

```bash
python train_model.py
```

The trained model is saved as:

```text
gesture_model.pkl
```

### 3. Live Prediction

Run the prediction script:

```bash
python live_predict.py
```

The model predicts gestures in real time and displays them on the web page.

---

## 📊 Dataset Format

```text
Flex1, Flex2, Flex3, Flex4, Flex5,
AccX, AccY, AccZ,
GyroX, GyroY, GyroZ,
Gesture_Label
```

Example:

```text
820,790,845,810,780,15,-8,1024,5,2,-3,HELLO
```

---

## ▶️ Installation & Usage

### Clone Repository

```bash
git clone https://github.com/yourusername/sign-language-translator.git
cd sign-language-translator
```

### Install Dependencies

```bash
pip install pandas scikit-learn joblib pyserial
```

### Collect Dataset

```bash
python data_collect.py
```

### Train Model

```bash
python train_model.py
```

### Run Live Prediction

```bash
python live_predict.py
```

---

## 🎯 Applications

- Assistive Communication
- Healthcare Technology
- Human Computer Interaction
- Smart Wearable Devices
- Sign Language Learning Systems

---

## 🔮 Future Enhancements

- Deep Learning Models (LSTM/CNN)
- Mobile Application Integration
- Wireless Wi-Fi Communication
- Multi-Language Speech Support
- Larger Gesture Vocabulary
- Cloud-Based Gesture Recognition

---

## 👨‍💻 Author

**Karthick**

B.E. Electronics and Telecommunication Engineering  
Karpagam College of Engineering

### Skills

- Embedded Systems
- IoT Development
- Machine Learning
- ESP32 Programming
- Raspberry Pi
- PCB Design

---

## ⭐ GitHub Description

Smart Sign Language Translator using ESP32, Raspberry Pi, Flex Sensors, MPU6050, and Random Forest Machine Learning. Converts hand gestures into real-time text and speech through a web interface for assistive communication.
