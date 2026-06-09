#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

// Flex sensor pins (as you used)
#define F1 34
#define F2 35
#define F3 32
#define F4 33
#define F5 25

void setup() {
  Serial.begin(115200);

  // MPU6050 init
  Wire.begin(21, 22);
  mpu.initialize();

  // Small delay for stability
  delay(1000);
}

void loop() {

  // 🔹 Read flex sensors
  int f1 = analogRead(F1);
  int f2 = analogRead(F2);
  int f3 = analogRead(F3);
  int f4 = analogRead(F4);
  int f5 = analogRead(F5);

  // 🔹 Read MPU6050
  int16_t ax, ay, az;
  int16_t gx, gy, gz;

  mpu.getAcceleration(&ax, &ay, &az);
  mpu.getRotation(&gx, &gy, &gz);

  // 🔥 IMPORTANT FORMAT (MATCH PYTHON)
  Serial.print("<");

  Serial.print(f1); Serial.print(",");
  Serial.print(f2); Serial.print(",");
  Serial.print(f3); Serial.print(",");
  Serial.print(f4); Serial.print(",");
  Serial.print(f5); Serial.print(",");

  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az); Serial.print(",");

  Serial.print(gx); Serial.print(",");
  Serial.print(gy); Serial.print(",");
  Serial.print(gz);

  Serial.println(">");

  // 🔥 VERY IMPORTANT → prevents buffer overload
  delay(200);
}