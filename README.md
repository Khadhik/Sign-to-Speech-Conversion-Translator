🤟 Sign Language to Speech Conversion Translator

A wearable IoT-based Sign Language Translator that converts hand gestures into readable text and speech output in real time. This system helps bridge the communication gap between speech/hearing-impaired individuals and others using machine learning and embedded systems.

📸 Project Overview
<img src="project_image.jpg" alt="Smart Sign Language Translator" width="400"/>

The system uses flex sensors and an MPU6050 motion sensor mounted on a glove to capture finger bending and hand movement data. An ESP32 collects the sensor readings and sends them to a Raspberry Pi, where a Machine Learning model predicts the corresponding gesture. The predicted gesture is displayed on a web interface and can be converted into speech.

🚀 Features
Real-time sign language recognition
Wearable smart glove design
ESP32-based sensor data acquisition
Raspberry Pi-based Machine Learning processing
Random Forest Classification model
Live web interface for gesture display
Text-to-Speech output support
Easy dataset collection and model retraining
🛠 Hardware Components
ESP32 Development Board
Raspberry Pi
5 × Flex Sensors
MPU6050 Accelerometer & Gyroscope
Hand Glove
Jumper Wires
Power Supply
💻 Software & Technologies
Python
Arduino IDE
ESP32
Raspberry Pi OS
Scikit-Learn
Random Forest Classifier
Pandas
Joblib
Serial Communication
📂 Project Structure
sign-language-translator/
│
├── data_collect.py        # Collects gesture data from ESP32
├── train_model.py         # Trains Random Forest model
├── live_predict.py        # Real-time gesture prediction
├── esp32.ino              # ESP32 sensor reading code
│
├── gesture_data.csv       # Dataset
├── gesture_model.pkl      # Trained model
│
├── templates/
│   └── index.html         # Web UI
│
├── static/
│   └── style.css          # Frontend styling
│
└── README.md
⚙ System Architecture
Flex Sensors + MPU6050
           │
           ▼
        ESP32
(Data Collection & Transmission)
           │
       Serial/WiFi
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
      ┌────┴────┐
      ▼         ▼
   Web Page   Speech
   Display    Output
📊 Machine Learning Workflow
1. Data Collection

The ESP32 reads:

5 Flex Sensor values
MPU6050 Accelerometer values
MPU6050 Gyroscope values

The data is transmitted to Raspberry Pi and stored using:

data_collect.py
2. Model Training

The collected dataset is used to train a Random Forest Classifier.

python train_model.py

The trained model is saved as:

gesture_model.pkl
3. Live Prediction

Real-time sensor data is sent from ESP32 to Raspberry Pi.

python live_predict.py

The model predicts the gesture and displays the output on the web page.

🧠 Machine Learning Model

Algorithm Used: Random Forest Classifier

Why Random Forest?
High accuracy
Fast prediction
Handles sensor noise effectively
Suitable for real-time embedded applications
📋 Dataset Format
Flex1, Flex2, Flex3, Flex4, Flex5,
AccX, AccY, AccZ,
GyroX, GyroY, GyroZ,
Gesture_Label

Example:

820,790,845,810,780,15,-8,1024,5,2,-3,HELLO
▶️ How to Run
Step 1: Upload ESP32 Code

Upload:

esp32.ino

using Arduino IDE.

Step 2: Collect Dataset
python data_collect.py

Enter gesture labels and collect training samples.

Step 3: Train Model
python train_model.py
Step 4: Start Live Prediction
python live_predict.py
Step 5: Open Web Interface

The predicted gesture will be displayed on the webpage and can be converted into speech.

🎯 Applications
Assistive Communication
Smart Healthcare Devices
Human Computer Interaction
Educational Tools
Sign Language Learning Systems
🔮 Future Improvements
Deep Learning Models (LSTM/CNN)
Wireless Communication using Wi-Fi
Mobile Application Integration
Multi-language Speech Output
Larger Gesture Vocabulary
Cloud-based Gesture Recognition
👨‍💻 Author

Karthick

B.E. Electronics and Telecommunication Engineering
Karpagam College of Engineering
