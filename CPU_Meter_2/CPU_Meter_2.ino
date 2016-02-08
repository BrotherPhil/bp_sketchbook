#define DIRECTION 2
#define MAGNITUDE 3
#include <Servo.h> 
Servo myservo;      // create servo object to control a servo 
Servo myservo2;      // create servo object to control a servo 
                        // a maximum of eight servo objects can be created 
int y = 90;

void setup() {
    Serial.begin(57600);
    
    myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
    myservo2.attach(10);
}

void loop() {
    int x = Serial.read();
    if (x == -1)
        return;
    y = ((y*9)+x)/10;
    myservo.write(180-x);              // tell servo to go to position in variable 'x' 
    myservo2.write(180-y);
    delay(250);                       // waits 0.25s for the servo to reach the position 
}

