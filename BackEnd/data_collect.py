import serial
import pandas as pd

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

buffer = ""

while True:
    try:
        label = input("\nEnter gesture label: ")
    except KeyboardInterrupt:
        print("\nExiting...")
        break

    data = []
    print("Collecting... Press Ctrl+C to stop this gesture")

    try:
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
                        values.append(label)
                        data.append(values)
                        print("Saved:", values)

                    except:
                        print("Skip bad data")

    except KeyboardInterrupt:
        if data:
            df = pd.DataFrame(data)
            df.to_csv("gesture_data.csv", mode='a', header=False, index=False)
            print(f"\nSaved {len(data)} samples for '{label}'")
        else:
            print("\nNo data collected!")