// Подключаем необходимые для работы библиотек
#include "MPU6050.h";
#include "I2Cdev.h";
#include "Wire.h";

// Создаем объект, символизирующий модуль датчика
MPU6050 axeler;

// Создаем объект библиотеки Wire
//Wire b;

// Создаем объект, который символизирует контакт I2C
I2Cdev h;

// Вводим цифровые данные, отвечающие за точки в 3-х осях
int16_t axx, axy, axz;
int16_t gix, giy, giz;

//#define b Serial

// Объявляем метод, который будет запускать программу
void setup()

{
// Начинаем работу
Wire.begin();
Serial.begin(38400);

// Производим инициализацию, отчет выводится после компиляции
Serial.println("Initializing I2C devices...");
axeler.initialize();
delay(100);
}

// Считываем значения гироскопа и акселерометра с помощью адресов, которые принадлежат описанным выше переменным
void loop()
{
axeler.getMotion6(&axx, &axy, &axz, &gix, &giy, &giz);

// Выводим получившиеся значения на экран
Serial.print("a/g:\t");
Serial.print(axx); 
Serial.print("\t");
Serial.print(axy);
Serial.print("\t");
Serial.print(axz); 
Serial.print("\t");
Serial.print(gix); 
Serial.print("\t");
Serial.print(giy); 
Serial.print("\t");
Serial.println(giz);
}
