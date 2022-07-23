byte trigP = 13;
byte echoP = 12;
byte ledp = 8;
byte ledv = 7;
byte leda = 4;

void setup()
{
  Serial.begin(9600);
  pinMode(trigP, OUTPUT);
  pinMode(echoP, INPUT);
  pinMode(ledp, OUTPUT);
  pinMode(ledv, OUTPUT);
  pinMode(leda, OUTPUT);
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
    else if(dist >= 60 && dist < 80){
    digitalWrite(ledv,HIGH);
    Serial.println("Arriba o igual a 60 pero menor a 80");
    Serial.print(dist);
    Serial.println("cm");
  }
    else if(dist >= 80 && dist < 100){
    digitalWrite(leda,HIGH);
    Serial.println("Arriba o igual a 80 pero menor a 100");
    Serial.print(dist);
    Serial.println("cm");
  }
   else{
      digitalWrite(ledp,HIGH);
      Serial.println("Arriba de 100");
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
