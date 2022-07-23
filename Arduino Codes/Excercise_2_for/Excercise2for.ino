// C++ code
//
void setup()
{
  Serial.begin(9600);
  
  pinMode(LED_BUILTIN, OUTPUT);
  
  
  for (int i=0; i<100; i++){
    Serial.println(i);
  }
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
}
