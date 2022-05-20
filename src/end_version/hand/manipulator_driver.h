// https://arduinoplus.ru/i2c-svyaz-arduino/

#include <Wire.h>

#define manipulator_address 0x04

void manipulator_driver_setup()
{
  Wire.begin(); // join I2C bus as Master
}

void send_data_to_manipulator(byte a, byte b)
{
  Wire.beginTransmission(manipulator_address);
  Wire.write(a);
  Wire.write(b);
  Wire.endTransmission();

  /*Wire.requestFrom(0x08, 1);    // request potentiometer position from slave 0x08
  if(Wire.available()) {        // read response from slave 0x08
    i2c_rcv = Wire.read();
  }*/
}
