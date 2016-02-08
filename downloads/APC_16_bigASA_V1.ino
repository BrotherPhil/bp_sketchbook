//------------------------------------------------------------------------------
//
//  APC Arduino Masterclass - Project #16 - Mono/Stereo Audio Spectrum Analyser
//
//  Written by Darren Yates 19-Feb-2014
//
//  Using:
//     * ArduinoFHT library from OpenMusicLabs
//     * 32x16-LED DMD from Freetronics
//     * Arduino Uno R3
//     * DIY Protoboard Shield
//
//-------------------------------------------------------------------------------

#define LIN_OUT 1
#define FHT_N 128 // set to 256 point fht

#include <FHT.h> // include the library
#include <SPI.h>
#include <DMD.h>        //
#include <TimerOne.h>   //
#include "SystemFont5x7.h"
#include "Arial_black_16.h"

#define DISPLAYS_ACROSS 1
#define DISPLAYS_DOWN 1
DMD dmd(DISPLAYS_ACROSS, DISPLAYS_DOWN);

//-------------------------------------------------------------------------------
// Change this to MONO to for a one-channel full-display or STEREO for two-channel
//
String displayType = "MONO";
//
// Change this to MONO to for a one-channel full-display or STEREO for two-channel
//-------------------------------------------------------------------------------

byte sampleR[64];
byte sampleL[64];
unsigned long startTime, endTime, oldTime;
String displayText = "DY";
String sampleSet;
int displaySize;

void setup() {

  if (displayType == "MONO") {displaySize = 32;} else {displaySize = 16;}
  
  //TIMSK0 = 0; // turn off timer0 for lower jitter
  ADCSRA = 0xe7; // set the adc to free running mode
  ADMUX = 0x45; // use adc5
  DIDR0 = 0x20; // turn off the digital input for adc5

  Timer1.initialize( 5000 );           //period in microseconds to call ScanDMD. Anything longer than 5000 (5ms) and you can see flicker.
  Timer1.attachInterrupt( ScanDMD );   //attach the Timer1 interrupt to ScanDMD which goes to dmd.scanDisplayBySPI()
  dmd.clearScreen( true );   //true is normal (all pixels off), false is negative (all pixels on)

  dmd.selectFont(Arial_Black_16); // show off who wrote the app... :p
  dmd.drawString(6,1,"DY",2,GRAPHICS_NORMAL);
  delay(3000);
  dmd.selectFont(SystemFont5x7);
  dmd.drawString(2,0,"Audio",5,GRAPHICS_NORMAL);
  dmd.drawString(2,9,"Spect",5,GRAPHICS_NORMAL);
  delay(3000);

}

void loop() {

  startTime = millis();
  sampleSet = "L";
  sampleInput();
  sampleFix();
  if (displaySize == 16) {
    sampleSet = "R";
    sampleInput();
    sampleFix();
  }
  drawSpectrum();
  endTime = millis();
}

void ScanDMD()
{ 
  dmd.scanDisplayBySPI();
}

void drawSpectrum () {

  if (displaySize == 16) {
    dmd.clearScreen(true);
    for (int disX; disX < 16; disX++) {
      dmd.drawLine (disX, 16, disX, 16-sampleL[disX+1], GRAPHICS_NORMAL );
      dmd.drawLine (17+disX, 16, 17+disX, 16-sampleR[disX+1], GRAPHICS_NORMAL );
    }
  } 
  else {
    dmd.clearScreen(true);
    for (int disX; disX < 33; disX++) {
      dmd.drawLine (disX, 16, disX, 16-sampleL[disX+1], GRAPHICS_NORMAL );
    }
  }

}

void sampleInput() {
  cli();  // UDRE interrupt slows this way down on arduino1.0
  for (int x=0; x<FHT_N; x++) {
    while(!(ADCSRA & 0x10)); // wait for adc to be ready
    ADCSRA = 0xf5; // restart adc
    if (sampleSet == "L") {
      ADMUX = 0x45; // use adc5
    } else {
      ADMUX = 0x44; // use adc4
    }
    byte m = ADCL; // fetch adc data
    byte j = ADCH;
    int k = (j << 8) | m; // form into an int
    k -= 0x0200; // form into a signed int
    k <<= 6; // form into a 16b signed int
    fht_input[x] = k; // put real data into bins
  }
  sei();
  fht_window(); // window the data for better frequency response
  fht_reorder(); // reorder the data before doing the fht
  fht_run(); // process the data in the fht
  fht_mag_lin();

}

void sampleFix() {

  int newPos; 
  float fhtCount, tempY;
  for (int x=0; x < displaySize; x++) {
    fhtCount = FHT_N/2;
    newPos = x * (fhtCount / displaySize); // single channel half-display 15-LED wide
    tempY = fht_lin_out[newPos]; 
    if (sampleSet == "L") {
    sampleL[x] = ((tempY/256)*16); // single channel full 16 LED high
    } else {
    sampleR[x] = ((tempY/256)*16); // single channel full 16 LED high
    }
  }  

} 


