
/*
 * Random Number Generator
 * Phil Culmer 2015


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
 
 This example code is in the public domain.
 
 */

// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

int digits = 9;
long x = 0;


void setup()                   
{
    // Set up Serial port
    Serial.begin(9600);
    // set up the LCD's number of columns and rows: 
    lcd.begin(16, 2);
    // Seed random nmber generator from (hopefully) floating ADC input
    randomSeed(analogRead(0));
}

void loop()                     // run over and over again
{
    x=random(1000000000);
    Serial.printf("%08d",x);
    lcd.clear();
    lcd.printf("%08d",x);
    delay(1000);
  }
 

