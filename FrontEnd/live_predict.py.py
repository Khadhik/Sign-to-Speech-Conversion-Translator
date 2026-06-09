import serial
import joblib
from collections import deque

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

model = joblib.load("gesture_model.pkl")

print("Live prediction started...")

buffer = ""
history = deque(maxlen=5)

while True:
    chunk = ser.read(64).decode('utf-8', errors='ignore')
    buffer += chunk

    while "<" in buffer and ">" in buffer:
        start = buffer.find("<")
        end = buffer.find(">", start)

        if end == -1:
            break

        packet = buffer[start+1:end]
        buffer = buffer[end+1:]

        values = packet.split(',')

        if len(values) == 11:
            try:
                values = list(map(int, values))

                prediction = model.predict([values])

                history.append(prediction[0])

                # 🔥 stable prediction
                if history.count(prediction[0]) >= 3:
                    print("Gesture:", prediction[0])

            except Exception as e:
                print("Error:", e)