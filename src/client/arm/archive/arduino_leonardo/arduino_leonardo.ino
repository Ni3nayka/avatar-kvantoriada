#define mut_R_pin A0

/*void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(mut_R_pin));
  delay(100);
}
*/

#include <Wire.h> // Must include Wire library for I2C
#include "SFE_MMA8452Q.h" // Includes the SFE_MMA8452Q library

MMA8452Q accel(0x1C);

void setup()
{
    Serial.begin(9600);
    Serial.println("MMA8452Q Test Code!");
    accel.init();
}

// The loop function will simply check for new data from the
//  accelerometer and print it out if it's available.
void loop()
{
    if (accel.available()) {
        accel.read();
        printAccels();
    
        Serial.println();
    }
}

void printAccels()
{
    Serial.print(accel.x);
    Serial.print(" ");
    Serial.print(accel.y);
    Serial.print(" ");
}
