#define DIRECTION 2
#define MAGNITUDE 3
#include <Servo.h> 
Servo myservo;      // create servo object to control a servo 
                        // a maximum of eight servo objects can be created 
                        
void setup() {
    Serial.begin(57600);
    
    myservo.attach(9);  // attaches the servo on pin 9 to the servo object 

}

void loop() {
    int x = Serial.read();
    if (x == -1)
        return;

    myservo.write(x);              // tell servo to go to position in variable 'x' 
    delay(250);                       // waits 0.25s for the servo to reach the position 
}

