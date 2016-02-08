#include <avr/pgmspace.h>
#include <SplitRadixRealT.h>

   SplitRadixRealT  splitRR;

#define VERTICAL        30

void print_charta( int data[], int dlina, int autosc )
{
  int peak = 0, nbr;
  const char mark = '*', nomk = '-';

  if ( autosc ) {
  for ( int i = 0; i < FFT_SIZE/dlina; i++)
   { if ( (data[i]) > peak ){
        peak = data[i];
        nbr = i;
       }
    }
  }
  else {
  peak = 90;
  nbr  = -1;
  }
  for ( int j = VERTICAL; j > 0; j-- )
            { Serial.print('|');
           for ( int i = 0; i < FFT_SIZE/dlina; i++)
            { if ((data[i]) >= j * (peak/VERTICAL)) {
                 Serial.print( mark);
                 delay(1);
            }
              else{
                 Serial.print( nomk);
                 delay(1);
              }
            }
           Serial.println('|');
        }
   Serial.print("\tPeak: ");
   Serial.print(peak);
   Serial.print("\t N: ");
   Serial.println(nbr);
}

//**************************************************************************************************

int   f_r[FFT_SIZE];
int   incomingByte; 

unsigned long time_start;
unsigned int  time_sampl, time_windw, time_revbn, time_splRR, time_gainR, time_magn1, time_magn2;

const int sdvig = 512; //DC bias of the ADC, approxim +2.5V.

void setup() {
  Serial.begin(115200);  
}

void sampling() {
  ADCSRA = 0x85;   // turn on adc, freq  = 1/32,   500 kHz/ 13.5 =~ 36 kHz sampling rate
  ADMUX = 0x40;    //Bit 5 – ADLAR: NO ADC Left Adjust Result
  ADCSRA |= (1<<ADSC);

  while(!(ADCSRA & 0x10));
  int sum2b;
  for(int i = 0; i < FFT_SIZE; i++ ) {
    while(!(ADCSRA & 0x10));
    ADCSRA |= (1<<ADSC);
    sum2b =  ADCL; 
    sum2b += (ADCH << 8);   
    f_r[i] = sum2b - sdvig;
  }  
  ADCSRA = 0x00;
}

void loop()
{
//Debugging monitor, to check processing data on each stage.

// x command - printout data received from ADC (input raw data).
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'x') {
    
    sampling();
    
      for (int i = 0; i < FFT_SIZE; i++){
        Serial.print("\t");
        Serial.print(f_r[i], DEC);
        if ((i+1)%16 == 0) Serial.print("\n");
      } 
      Serial.print("\n");
      delay(200);
    }

// f command - printout data after FFT. Clear view of each bin in the spectrum.
// ---->>>>>   Both format, as a table and chart representation   <<<<<-------
// Chart is AUTOSCALE mode, pay attention to the magnitude printed at the bottom.
  if (incomingByte == 'f') {

// 1.Sampling
  time_start = micros();
   sampling(); 
  time_sampl  = micros() - time_start;

// 2.Windowing
  time_start = micros();
   for ( uint16_t i = 0, k = (NWAVE / FFT_SIZE); i < FFT_SIZE; i++ ) 
   {  
      int16_t windw = pgm_read_word(&Hamming[i * k]);
      f_r[i] = mult_shf_s16x16(f_r[i], windw);
   }
  time_windw  = micros() - time_start;

// 3.RevBin
  time_start = micros();
   splitRR.rev_bin( f_r, FFT_SIZE);
  time_revbn  = micros() - time_start;

// 4. FFT - SplitRadixReal in place.
  time_start = micros();
   splitRR.fft_split_radix_real( f_r, LOG2_FFT); 
  time_splRR  = micros() - time_start;

// 5. Gain Reset
  time_start = micros();
   splitRR.gain_Reset( f_r, LOG2_FFT -1);
  time_gainR  = micros() - time_start;

      for (int i = 0; i < FFT_SIZE; i++){
        Serial.print("\t");
        Serial.print(f_r[i], DEC);
        if ((i+1)%16 == 0) Serial.print("\n");
      } 
      Serial.print("\n");

// Choose 6 or 7, Commenting out unused. 
/*
// 6. Magnitude calculation - precise sqrt, slow.
  time_start = micros();
   splitRR.get_Magnit1( f_r); 
  time_magn1  = micros() - time_start;
*/

// 7. Magnitude calculation - approximation, fast.
  time_start = micros();
   splitRR.get_Magnit2( f_r); 
  time_magn2  = micros() - time_start;

      for (int i=0; i < (FFT_SIZE / 2); i++){
        Serial.print("\t");
        Serial.print(f_r[i], DEC);     
        if ((i+1)%16 == 0) Serial.print("\n");
      } // Print out Magnitudes
      delay(200);
      Serial.print("\n");

     Serial.print("\tSmpl ");
     Serial.print(time_sampl);
     Serial.print("\tWind ");
     Serial.print(time_windw);
     Serial.print("\tRevb ");
     Serial.print(time_revbn);
     Serial.print("\tSplitRR_T ");
     Serial.print(time_splRR);
     Serial.print("\tGainR ");
     Serial.print(time_gainR);
     Serial.print("\tMagnit1 ");
     Serial.print(time_magn1);
     Serial.print("\tMagnit2 ");
     Serial.println(time_magn2);
  
     print_charta( f_r, 2, 1 );
  }
 }
}
