// Code provided by Smoke And Wires
// http://www.smokeandwires.co.nz
// This code has been taken from the Adafruit TFT Library and modified
//  by us for use with our TFT Shields / Modules
// For original code / licensing please refer to
// https://github.com/adafruit/TFTLCD-Library

#include <Adafruit_GFX.h>    // Core graphics library
#include "SWTFT.h" // Hardware-specific library

// The control pins for the LCD can be assigned to any digital or
// analog pins...but we'll use the analog pins as this allows us to
// double up the pins with the touch screen (see the TFT paint example).
// #define LCD_CS A3 // Chip Select goes to Analog 3
// #define LCD_CD A2 // Command/Data goes to Analog 2
// #define LCD_WR A1 // LCD Write goes to Analog 1
// #define LCD_RD A0 // LCD Read goes to Analog 0

// #define LCD_RESET A4 // Can alternately just connect to Arduino's reset pin

// When using the BREAKOUT BOARD only, use these 8 data lines to the LCD:
// For the Arduino Uno, Duemilanove, Diecimila, etc.:
//   D0 connects to digital pin 8  (Notice these are
//   D1 connects to digital pin 9   NOT in order!)
//   D2 connects to digital pin 2
//   D3 connects to digital pin 3
//   D4 connects to digital pin 4
//   D5 connects to digital pin 5
//   D6 connects to digital pin 6
//   D7 connects to digital pin 7
// For the Arduino Mega, use digital pins 22 through 29
// (on the 2-row header at the end of the board).

// Assign human-readable names to some common 16-bit color values:
#define	BLACK   0x0000
#define	BLUE    0x001F
#define	RED     0xF800
#define	GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

SWTFT tft;
// If using the shield, all control and data lines are fixed, and
// a simpler declaration can optionally be used:
// SWTFT tft;

void setup(void) {
  Serial.begin(9600);
  tft.reset();
  tft.fillScreen(BLACK);
  tft.setTextColor(GREEN);
  Serial.println("Ready.");
}

void loop()
{
  // when characters arrive over the serial port...
  if (Serial.available()) {
    // wait a bit for the entire message to arrive
    delay(100);
    tft.setTextColor(GREEN);
    tft.setTextSize(2);
    // read all the available characters
    while (Serial.available() > 0) {
      // display each character to the LCD
      tft.print(Serial.read());
    }
  }
}

