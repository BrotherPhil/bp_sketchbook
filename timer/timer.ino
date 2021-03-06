#include <elapsedMillis.h>
// see warning above about FioV3
int led = 13;  
// Pin 13 has an LED connected on most Arduino boards.
// if using Arduino IDE 1.5 or above you can use pre-defined
// LED_BUILTIN  instead of 'led'
// 
elapsedMillis timer0;
#define interval 1000
// the interval in mS 

// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  timer0 = 0; // clear the timer at the end of startup
}

void loop() {
  if (timer0 > interval) {
    timer0 -= interval; //reset the timer
    int ledPin = digitalRead(led);
    // read the current state and write the opposite
    digitalWrite(led, !ledPin);
  }
}
