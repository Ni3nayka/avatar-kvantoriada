// https://www.youtube.com/watch?v=2NQ7uOMNEIs
#include <AnalogKey.h> 
#include <Joystick.h> 
Joystick_ Joystick;

int zAxis_ = 0; 
int RxAxis_ = 0;    
int RyAxis_ = 0;                      
int RzAxis_ = 0;          
int Throttle_ = 0;
int xAxis_ = 0;
int val;

const bool initAutoSendState = true; 

void setup() {
pinMode(0, INPUT_PULLUP); 
pinMode(1, INPUT_PULLUP); 
pinMode(2, INPUT_PULLUP);
pinMode(3, INPUT_PULLUP);
pinMode(4, INPUT_PULLUP); 
pinMode(5, INPUT_PULLUP);
pinMode(6, INPUT_PULLUP);
pinMode(7, INPUT_PULLUP); 
pinMode(8, INPUT_PULLUP);
pinMode(9, INPUT_PULLUP);
pinMode(10, INPUT_PULLUP);
pinMode(11, INPUT_PULLUP);
pinMode(12, INPUT_PULLUP);
pinMode(13, INPUT_PULLUP);


Serial.begin(9600);


Joystick.begin();
}

// Constant that maps the phyical pin to the joystick button.
const int pinToButtonMap = 0;
// Last state of the button
int lastButtonState[14] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0};


void loop() {
  
xAxis_ = analogRead(A5);
xAxis_ = map(xAxis_,1023,0, 1023, 0);            
Joystick.setXAxis(xAxis_);

zAxis_ = analogRead(A0);  
zAxis_ = map(zAxis_,0,1023,0,1023);
Joystick.setZAxis(zAxis_); 
  
RxAxis_ = analogRead(A1);
 RxAxis_ = map(RxAxis_,0,1023,0,1023);
 Joystick.setRxAxis(RxAxis_);
  
 RyAxis_ = analogRead(A2);
 RyAxis_ = map(RyAxis_,0,1023,0,1023);
 Joystick.setRyAxis(RyAxis_);

 RzAxis_ = analogRead(A3);
 RzAxis_ = map(RzAxis_,1023,0,1023,0);            
Joystick.setRzAxis(RzAxis_);

Throttle_ = analogRead(A4);
Throttle_ = map(Throttle_,1023,0,1023,0);         
Joystick.setThrottle(Throttle_);   

// Read pin values
  for (int index = 0; index < 14; index++)
  {
    int currentButtonState = !digitalRead(index + pinToButtonMap);
    if (currentButtonState != lastButtonState[index])
    {
      Joystick.setButton(index, currentButtonState);
      lastButtonState[index] = currentButtonState;
    }
  }


}
