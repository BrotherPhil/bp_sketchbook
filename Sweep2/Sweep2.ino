// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo1;  // create servo object to control a servo 
Servo myservo2;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
int poss = 90;  // sin motor
int posc = 90;   // cos motor
 
void setup() 
{ 
  myservo1.attach(10);  // attaches the servo on pin 10 to the servo1 object 
  myservo2.attach(9);  // attaches the servo on pin 9 to the servo2 object 

} 
 
 
void loop() 
{ 
  for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees 
  {        // in steps of 1 degree 
    poss=90 + (90*sin(pos));
    posc=90 + (90*cos(pos));
    
    myservo1.write(poss);              // tell servo to go to position in variable 'pos' 
    myservo2.write(posc);              // tell servo to go to position in variable 'pos' 
    delay(150);                       // waits 15ms for the servo to reach the position 
  } 
  for(pos = 180; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees 
 {        // in steps of 1 degree 
    poss=90 + (90*sin(pos));
    posc=90 + (90*cos(pos));
    
    myservo1.write(poss);              // tell servo to go to position in variable 'pos' 
    myservo2.write(posc);              // tell servo to go to position in variable 'pos' 
    delay(150);                       // waits 15ms for the servo to reach the position 
  } 
 
} 
