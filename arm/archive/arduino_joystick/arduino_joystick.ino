// https://www.youtube.com/watch?v=2NQ7uOMNEIs
/*          
Joystick.setXAxis(xAxis_);
Joystick.setZAxis(zAxis_); 
 Joystick.setRxAxis(RxAxis_);
 Joystick.setRyAxis(RyAxis_);           
Joystick.setRzAxis(RzAxis_);       
Joystick.setThrottle(Throttle_);  
Joystick.setButton(n, 1); 
*/

#include "Joystick.h"
Joystick_ Joystick;

#define mut_R_pin A0
#define joystick_x_pin A1
#define joystick_y_pin A2
#define joystick_button_pin A3

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
  // setup arduino to joystick
  Joystick.begin();
}

void loop() {
  /*Serial.print(analogRead(A1));
  Serial.print(" ");
  Serial.println(analogRead(A2));
  delay(100);*/
  
  // elbow          
  Joystick.setZAxis(analogRead(mut_R_pin));     
  // joystick
  Joystick.setXAxis(analogRead(joystick_x_pin));        
  Joystick.setYAxis(analogRead(joystick_y_pin));
  Joystick.setButton(0, !digitalRead(joystick_button_pin));
  // akselerometr
  int angle_ax, angle_ay;
  read_akselerometr(1,angle_ax,angle_ay);
  //Joystick.setZAxis(map(angle_ax,-90,90,0,1023));
  Joystick.setRxAxis(map(angle_ax,-90,90,0,1023));
  Joystick.setRyAxis(map(angle_ay,-90,90,0,1023));
  //Joystick.setRxAxis(0);
  //Joystick.setRyAxis(0);
  read_akselerometr(0,angle_ax,angle_ay);
  Joystick.setRzAxis(map(angle_ay,-90,90,0,1023)); 
}
