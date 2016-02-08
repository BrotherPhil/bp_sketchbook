#define LED 13
//#define Sounder 10
#define Button 7
#include <Servo.h> 
Servo myservo1;  // create servo object to control a servo 
Servo myservo2;  // create servo object to control a servo 

int key=0;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(Button,INPUT);
  myservo1.attach(10);  // attaches the servo on pin 10 to the servo1 object 
  myservo2.attach(11);  // attaches the servo on pin 9 to the servo2 object 
}

void loop() {
  key=digitalRead(Button);
  
  if (key == HIGH) {
    digitalWrite(LED,HIGH);
    myservo1.write(90);
    myservo2.write(90);
  }
  else {
    digitalWrite(LED,LOW);
    myservo1.write(0);
    myservo2.write(0);

  }
} 
