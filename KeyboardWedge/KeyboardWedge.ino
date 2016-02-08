/* 
 Keyboard wedge
 
 For the Arduino Leonardo or Micro
 
 Reads a byte from the serial port, sends a keystroke back.

  LiquidCrystal Library - Serial Input
 
 Demonstrates the use a 16x2 LCD display.  The LiquidCrystal
 library works with all LCD displays that are compatible with the 
 Hitachi HD44780 driver. There are many of them out there, and you
 can usually tell them by the 16-pin interface.
 
The circuit:
 * LCD RS pin to digital pin 8
 * LCD Enable pin to digital pin 9
 * LCD D4 pin to digital pin 4
 * LCD D5 pin to digital pin 5
 * LCD D6 pin to digital pin 6
 * LCD D7 pin to digital pin 7
 * LCD R/W pin to ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)
 
 Library originally added 18 Apr 2008
 by David A. Mellis
 library modified 5 Jul 2009
 by Limor Fried (http://www.ladyada.net)
 example added 9 Jul 2009
 by Tom Igoe 
 modified 22 Nov 2010
 by Tom Igoe
 

 created 21 Oct 2011
 modified 27 Mar 2012
 by Tom Igoe
 
This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/KeyboardSerial
 */
 
// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() {
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  // open the serial port:
  Serial.begin(9600);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // check for incoming serial data:
  if (Serial.available() > 0) {
    // read incoming serial data:
    char inChar = Serial.read();
    // Type what you received:
    Keyboard.write(inChar);
    lcd.setCursor(0,15);
    lcd.write(inChar);
    lcd.scrollDisplayLeft(); 
 
  }  
}

