#define led_1 13
#define led_2 12

void setup() {
  Serial.begin(9600);
  pinMode(led_1,OUTPUT);
  pinMode(led_2,OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char t = Serial.read();
    if      (t=='S') { digitalWrite(led_1,0); digitalWrite(led_2,0); }
    else if (t=='F') { digitalWrite(led_1,1); digitalWrite(led_2,0); }
    else if (t=='B') { digitalWrite(led_1,0); digitalWrite(led_2,1); }
  }
}
