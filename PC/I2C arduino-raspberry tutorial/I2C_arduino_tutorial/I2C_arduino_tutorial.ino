// I2C - протокол связи, по которому можно связать arduino и raspberry

#include <Wire.h>              // подключаем библиотеку

#define MY_ADDRESS  0x04       // I2C адресс arduino

// если хотим принимать не значения (0-255) а буквы, то нам надо задать не byte, а char
byte in_data = 0;              // переменная для приема данных с raspberry 
byte out_data = 0;             // переменная для передачи данных на raspberry

void setup() {                 // установочная подпрограмма
  Serial.begin(9600);          // запускаем Serial для вывода информации в монитор порта
  Wire.begin(MY_ADDRESS);      // присваиваем ардуине (себе) этот I2C адресс
  Wire.onReceive(read_data);   // запускаем прием данных
  Wire.onRequest(write_data);  // запускаем отправку данных
}                              // оба предыдущих пункта работают на прерывании, поэтому их не надо отдельно вызывать

void loop() {                  // основной цикл программы
                               // здесь пусто, т.к. нам ничего кроме приема\отправки данных пока не надо
}

void read_data() {             // подпрограмма приема данных
  in_data = int(Wire.read());  // прием данных
  //in_data = Wire.read();     // отправить\получить можно не только byte, а еще и char (букву)
  Serial.print("in_data: ");   // вывод данных в Serial
  Serial.println(in_data);     // вывод данных в Serial
}
 
void write_data() {            // подпрограмма отправки данных 
  out_data = random(0, 255);   // придумываем значение для отправки
  Wire.write(out_data);        // отправка данных
  Serial.print("out_data: ");  // вывод данных в Serial
  Serial.println(out_data);    // вывод данных в Serial
}


