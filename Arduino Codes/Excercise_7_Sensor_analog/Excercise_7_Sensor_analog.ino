// Declaracion de variables globales
float tempC; // Variable para almacenar el valor obtenido del sensor (0 a 1023)
float tempCbits; //
float tempCvolts; //

void setup() {
  // Configuramos el puerto serial a 9600 bps
  Serial.begin(9600);
 
}
 
void loop() {
  // Con analogRead leemos el sensor, recuerda que es un valor de 0 a 1023
  tempCbits = analogRead(A1); 
   
  // Calculamos la temperatura con la fórmula
  //tempCvolts = (tempCbits / 1023.0) * 5;
  tempCvolts = (tempCbits / 318) * 50;
 
  Serial.print("Bits: ");
  Serial.print(tempCbits);
  // Salto de línea
  Serial.print("\n");
  // Envia el dato al puerto serial
  Serial.print("Temperatura: ");
  Serial.print(tempCvolts);
  Serial.print(" C ");
  // Salto de línea
  Serial.print("\n");
  
  
  // Esperamos un tiempo para repetir el loop
  delay(1000);
}
