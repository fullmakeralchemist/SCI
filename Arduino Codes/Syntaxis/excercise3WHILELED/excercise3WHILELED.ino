int pinLed = 11;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pinLed, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int var = 0;

  while(var <255) {
    analogWrite(pinLed, var);
     delay(100);

     var++;
  }

}
