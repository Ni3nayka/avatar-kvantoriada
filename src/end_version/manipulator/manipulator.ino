#include <Servo.h>
#include <Wire.h>  

Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;
Servo myservo6;

int FLAG = 0;
unsigned long int time = 0; 
#define delta_t 30

#define MY_ADDRESS  0x04       // I2C адресс arduino
int pos_real[6] = {90,90,90,90,90,90};
int pos[6] = {0};
int wire_in = -1;
bool device[2] = {0,0}; // rele+mosfet

#define button 2
#define rele 10
#define mosfet 11

void setup() {
  Serial.begin(9600);

  for (int i=0; i<6; i++) pos[i] = pos_real[i];
  
  Wire.begin(MY_ADDRESS);      // присваиваем ардуине (себе) этот I2C адресс
  Wire.onReceive(read_data);   // запускаем прием данных
  Wire.onRequest(write_data);  // запускаем отправку данных
  
  myservo1.attach(4);
  myservo2.attach(5);
  myservo3.attach(6);
  myservo4.attach(7);
  myservo5.attach(8);
  myservo6.attach(9);
  
  pinMode(button,INPUT_PULLUP);
  pinMode(rele, OUTPUT);
  pinMode(mosfet, OUTPUT);
  //attachInterrupt(0, myEventListener, FALLING);
}



void loop() {
  if (digitalRead(button)==0) ending(); 
  if (time+delta_t<millis())write_servo();
  //digitalWrite(rele,1);digitalWrite(mosfet,1);delay(3000); digitalWrite(rele,0);digitalWrite(mosfet,0);delay(1000);
  digitalWrite(rele,device[0]);
  digitalWrite(mosfet,device[1]);
}


/*
 * protocol:
 * 2 bytes: number_device, state_device
 * if number_device(a)=[0..10) => servo[a]
 * if number_device(a)=[10..) => more_device(device)[a-10]
 */

void read_data() {             // подпрограмма приема данных
  if (wire_in==-1) wire_in = int(Wire.read());
  else {
    if (wire_in<10) pos[wire_in] = int(Wire.read());
    else device[wire_in-10] = int(Wire.read());
    wire_in = -1;
  }
}
 
void write_data() {            // подпрограмма отправки данных 
  int out_data = random(0, 255);   // придумываем значение для отправки
  Wire.write(out_data);        // отправка данных
  Serial.print("out_data: ");  // вывод данных в Serial
  Serial.println(out_data);    // вывод данных в Serial
}

void write_servo() {
  Serial.println(millis());

  for (int i=0; i<6; i++) {
    if      (pos[i]>pos_real[i]) pos_real[i]++;
    else if (pos[i]<pos_real[i]) pos_real[i]--;
  }
  
  myservo1.write(pos_real[0]);
  myservo2.write(pos_real[1]);
  myservo3.write(pos_real[2]);
  myservo4.write(pos_real[3]);
  myservo5.write(pos_real[4]);
  myservo6.write(pos_real[5]);

  time = millis();
}

void ending() {
  Serial.println("end");
  myservo1.detach();
  myservo2.detach();
  myservo3.detach();
  myservo4.detach();
  myservo5.detach();
  myservo6.detach();
  while(1);
}