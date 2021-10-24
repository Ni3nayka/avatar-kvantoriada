// include library
#include "Wire.h"

// akselerometr const
#define count_addr 2
int MPU_addr[2] = {0x68,0x69};

// work const
#define TO_DEG 57.29577951308232087679815481410517033f

//setup function
void setup_akselerometr();
void read_akselerometr(int n, int &angle_ax, int &angle_ay);
int operating_akselerometr_data(int ax_raw);
void getData(int n, int &ax_raw, int &ay_raw);

void setup_akselerometr() {
  // setup wire
  Wire.begin();
  // setup akselerometr - i2c
  for (int i=0; i<count_addr; i++) { 
    Wire.beginTransmission(MPU_addr[i]);
    Wire.write(0x6B); // PWR_MGMT_1 register
    Wire.write(0);    // set to zero (wakes up the MPU-6050)
    Wire.endTransmission(true);
  }
}

void read_akselerometr(int n, int &angle_ax, int &angle_ay) { // read data from akselerometr
  int ax_raw, ay_raw;
  // read data from akselerometr
  getData(MPU_addr[n],ax_raw,ay_raw);
  // return
  angle_ax = operating_akselerometr_data(ax_raw);
  angle_ay = operating_akselerometr_data(ay_raw);
}

int operating_akselerometr_data(int ax_raw) { // convect input data to gradus
  // convert input data to fraction
  float ax = ax_raw/16384.;
  if (ax>1) ax = 1;
  else if (ax<-1) ax = -1;
  //  convert fraction to gradus
  if (ax>=0) return 90 - TO_DEG*acos(ax);
  else return TO_DEG*acos(-ax) - 90;
}

void getData(int n, int &ax_raw, int &ay_raw) { // read data from akselerometr on i2c
  // setup
  Wire.beginTransmission(n);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(n, 14, true); // request a total of 14 registers
  // read data
  int16_t data[7]; 
  for (byte i = 0; i < 7; i++) {
    data[i] = Wire.read() << 8 | Wire.read();
  }
  // return
  ax_raw = data[1];
  ay_raw = data[0];
}
