int sensorTemp = 32;

void setup() {
  // put your setup code here, to run once:
  /*
   * Baud rate is commonly 
   * used when discussing electronics that use serial communication. 
   * In the serial port context, "9600 baud" means that the serial 
   * port is capable of transferring a maximum of 9600 bits per second.
   */
  Serial.begin(9600);
  if(sensorTemp > 32){
    Serial.print("Es un dia caluroso");
  } else {
    Serial.print("Es un clima agradable");
  }

}

void loop() {
  // put your main code here, to run repeatedly:

}
