/*
 * Declaracion de variables
 */

int sum;

byte var1 = 10;
byte var2 = 8;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);

  //SUMA
  suma = var1 + var2;
  Serial.print(res);

  //Agregar Resta

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH);
  delay(1000); //Wait for 1000 miliseconds or one second
  digitalWrite(13, LOW);
  delay(1000); //Wait for 1000 miliseconds or one second
}
