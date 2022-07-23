/*
 * This excercise is about 
 * the conditions interacting with 
 * LED
 */

int sensorTemp = 32;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);

  if(sensorTemp >= 32{
    Serial.print("Es un dia caluroso");
    digitalWrite(13, HIGH);
  } else {
    Serial.print("Es un clima agradable");
    digitalWrite(13, LOW);
  }

}

void loop() {
  // put your main code here, to run repeatedly:

}
