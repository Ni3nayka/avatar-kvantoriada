#define mut_R_pin A0
#define joystick_x_pin A1
#define joystick_y_pin A2
#define joystick_button_pin 4

#include "akselerometr.h"

// work const
#define delta_t 200

// working variable
unsigned long int time;

void setup() {
  // setup com port
  Serial.begin(9600);
  // setup digital pin
  pinMode(joystick_button_pin,INPUT_PULLUP);
  // setup akselerometr - i2c
  setup_akselerometr();
}

void loop() {
  /*Serial.print(analogRead(A1));
  Serial.print(" ");
  Serial.println(analogRead(A2));
  delay(100);*/
  if (Serial.available()) {
    Serial.read();
    // elbow        
    Serial.print(analogRead(mut_R_pin)); Serial.print(" ");
    // joystick
    Serial.print(analogRead(joystick_x_pin)); Serial.print(" ");
    Serial.print(analogRead(joystick_y_pin)); Serial.print(" "); 
    Serial.print(!digitalRead(joystick_button_pin)); Serial.print(" "); 
    // akselerometr
    int angle_ax, angle_ay;
    read_akselerometr(1,angle_ax,angle_ay);
    Serial.print(angle_ax); Serial.print(" ");
    Serial.print(angle_ay); Serial.print(" ");
    read_akselerometr(0,angle_ax,angle_ay);
    Serial.print(angle_ay); Serial.print(" "); 
    Serial.println();
  }
}
