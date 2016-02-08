/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 #include <Servo.h> 
 
Servo myservo1;  // create servo object to control a servo 
Servo myservo2;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 


// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  myservo1.write(180);           // tell servo to go to position in variable 'pos' 
  myservo2.write(0);             // tell servo to go to position in variable 'pos' 

  
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
  myservo1.write(90);              // tell servo to go to position in variable 'pos' 
  myservo2.write(90);              // tell servo to go to position in variable 'pos' 
}
