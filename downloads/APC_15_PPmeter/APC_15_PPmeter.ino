//------------------------------------------------------------
//
//     Stereo Peak Program Meter
//     Developed by Darren Yates for APC Magazine, 24-Jan-2014
//
//------------------------------------------------------------

#include <math.h>

int ppmArray[] = {2,3,4,5,6,7,8,9,10,11,12,13};
float dBAudio;
float newZero = 512;
int ch = 0;
int dbPerLed = 3;

void setup() {
  analogReference(INTERNAL);
  for (int ledCount = 0; ledCount < 12; ledCount++)  {
    pinMode (ppmArray[ledCount],OUTPUT);
  }
}

void loop() {
    ch = !ch;
    getPPMsample();
    if (ch==0) { digitalWrite(12,LOW); PORTD = B00000000; PORTB = PINB & B11000000; digitalWrite(13,HIGH); }
    else { digitalWrite(13,LOW); PORTD = B00000000; PORTB = PINB & B11000000; digitalWrite(12,HIGH); }
    for (int led = 0; led < 10; led++) {
      if (abs(dBAudio) <= (led*dbPerLed)+0.1 ) {digitalWrite (ppmArray[led], HIGH); } else {digitalWrite (ppmArray[led],LOW); } 
    }
  }    

void getPPMsample() {
  float maxAudio = 0; float rawAudio;
  for (int sample = 0; sample < 48; sample++) {
    if (ch==0) { rawAudio = analogRead(A0); } else { rawAudio = analogRead(A1); }    
    if (rawAudio > maxAudio) { maxAudio = rawAudio; }
  }
  dBAudio = 20 * log10 (abs(maxAudio-newZero)/newZero);
}

    
  

    
