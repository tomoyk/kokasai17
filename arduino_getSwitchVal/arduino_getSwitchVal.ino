#define SENSOR_PIN 7

void setup(){
  Serial.begin(9600);
}

void loop(){
  int val = digitalRead(SENSOR_PIN);
  Serial.write(val);
  delay(100);
}
