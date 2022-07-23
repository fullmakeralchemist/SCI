byte trigP = 13;
byte echoP = 12;
byte ledp = 8;

void setup()
{
  Serial.begin(9600);
  pinMode(trigP, OUTPUT);
  pinMode(echoP, INPUT);
  pinMode(ledp, OUTPUT);
}

void loop()
{
  long dur, dist;
  
  digitalWrite(trigP, LOW);
  delayMicroseconds(2);
  digitalWrite(trigP, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigP, LOW);
  
  dur = pulseIn(echoP, HIGH);
  dist = (dur/2)/29.1;
  
  if(dist<60){
    digitalWrite(ledp,LOW);
    Serial.println("Abajo de 60");
    Serial.print(dist);
    Serial.println("cm");
  }
    else{
      digitalWrite(ledp,HIGH);
      Serial.println("Arriba de 60");
      Serial.print(dist);
      Serial.println("cm");
      ///Serial.print(a);
//Serial.print(",");
//Serial.print(b);
//Serial.print(",");
//Serial.println(c);
    }
  delay(500);     
  
}
