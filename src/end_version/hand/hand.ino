#define mut_R_pin A0
#define joystick_x_pin A1
#define joystick_y_pin A2
#define joystick_button_pin 3

#include "akselerometr.h"
#include "manipulator_driver.h"

// work const
#define delta_t 200
#define motor 10

// working variable
unsigned long int time;
bool button_flag = 0;
bool button_history = 0;

int zero_servo = 90;

void setup() {
  // setup com port
  Serial.begin(9600);
  // setup digital pin
  pinMode(joystick_button_pin,INPUT_PULLUP);
  pinMode(motor,OUTPUT);
  // setup akselerometr - i2c
  setup_akselerometr();
}

void loop() {
  if (time+delta_t<millis()) {
    // elbow        
    send_data_to_manipulator(2,map(analogRead(mut_R_pin),0,1023,0,180));
    // joystick
    zero_servo += map(analogRead(joystick_x_pin),0,1023,-5,5);
    send_data_to_manipulator(0,zero_servo);
    //send_data_to_manipulator(2,analogRead(joystick_y_pin));
    send_data_to_manipulator(10,button_flag);
    // akselerometr
    int angle_ax, angle_ay;
    read_akselerometr(1,angle_ax,angle_ay);
    send_data_to_manipulator(4,angle_ax);
    send_data_to_manipulator(3,angle_ay);
    read_akselerometr(0,angle_ax,angle_ay);
    send_data_to_manipulator(1,angle_ay);
  }
  
  if (button_history && !digitalRead(joystick_button_pin)) {
    button_flag = !button_flag;
    //digitalWrite(motor,button_flag);
    //delay(100);
    send_data_to_manipulator(10,button_flag);
  }
  button_history = digitalRead(joystick_button_pin);
  
  if (Serial.available()) {
    Serial.read();
    // elbow        
    Serial.print(analogRead(mut_R_pin)); Serial.print(" ");
    // joystick
    Serial.print(analogRead(joystick_x_pin)); Serial.print(" ");
    Serial.print(analogRead(joystick_y_pin)); Serial.print(" "); 
    Serial.print(button_flag); Serial.print(" "); 
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
