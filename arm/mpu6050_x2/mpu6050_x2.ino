#include "akselerometr.h"

// work const
#define delta_t 200

// working variable
unsigned long int time;

void setup() {
  // setup akselerometr - i2c
  setup_akselerometr();
  // setup com port
  Serial.begin(9600);
}

void loop() {
  // test
  if (time+delta_t<millis()) {
    for (int i=0; i<count_addr; i++) { 
      int angle_ax, angle_ay;
      read_akselerometr(i,angle_ax,angle_ay);
      Serial.print(i+1);
      Serial.print(". ");
      Serial.print(angle_ax);
      Serial.print(" ");
      Serial.print(angle_ay);
      Serial.print(" ");
    }
    Serial.println();
    time = millis();
  }
}
