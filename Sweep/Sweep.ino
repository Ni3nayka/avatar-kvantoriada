/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo1;  // create servo object to control a servo
Servo myservo2;  // create servo object to control a servo
Servo myservo3;  // create servo object to control a servo
Servo myservo4;  // create servo object to control a servo
Servo myservo5;  // create servo object to control a servo
Servo myservo6;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position

void setup() {
  myservo1.attach(4);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(5);  // attaches the servo on pin 9 to the servo object
  myservo3.attach(6);  // attaches the servo on pin 9 to the servo object
  myservo4.attach(7);  // attaches the servo on pin 9 to the servo object
  myservo5.attach(8);  // attaches the servo on pin 9 to the servo object
  myservo6.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(2,INPUT_PULLUP);
  while (digitalRead(2)==1);
}

void loop() {
  /*for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }*/
  myservo1.write(pos);
  myservo2.write(pos);
  myservo3.write(pos);
  myservo4.write(pos);
  myservo5.write(pos);
  myservo6.write(pos);
}
