#include <Servo.h>

int pos = 0;

Servo servo_9;

void setup()
{
  
  servo_9.attach(9);
}

void loop()
{
  // sweep the servo from 0 to 180 degrees in steps
  // of 1 degrees
    // tell servo to go to position in variable 'pos'
  servo_9.write(180);
    // wait 15 ms for servo to reach the position
  delay(2500); // Wait for 15 millisecond(s)

    // tell servo to go to position in variable 'pos'
  servo_9.write(0);
    // wait 15 ms for servo to reach the position
  delay(2500); // Wait for 15 millisecond(s)
}
