/*
 *  original Fortran code by Sorensen; published in H.V. Sorensen, D.L. Jones,
 * M.T. Heideman, C.S. Burrus(1987)Real-valued fast fourier transform
 * algorithms.  IEEE Trans on Acoustics, Speech, & Signal Processing, 35,
 * 849-863.  Adapted to C by Bill Simpson, 1995  wsimpson@uwinnipeg.ca
 * derived from: static char RCSreal2herm_c[] =
 * "$Id: real2herm.c,v 1.1 1996/09/02 01:47:12 wedgingt Beta $";
 * further optimizations by Joerg Arndt  arndt@jjj.de
 * Adapted and optimized for Arduino UNO (8-bit uCPU)
 * by Anatoly Kuzmenko  k_anatoly@hotmail.com
 */
/*
 ***************   Split Radix Real FFT LIBRARY (UNO version) *****************
 * http://coolarduino.wordpress.com
 *
 * Created for Arduino UNO & like boards, word size optimized for 9-bits data input.
 * 
 * FFT takes as input ANY size of inputs array 8, 16, 32, 64, 128, 256, 512.
 * Max. size 512 defined by LUT (and uCPU memory limits). 
 *
 * Library may run on different platform, only variable declaration
 * type may need to be adjusted accordingly. Same with PROGMEM macros.
 *
 * Algorithm tested on Arduino UNO and IDE 1.0.5 (Tested on Linux OS only).
 *
 * Timing results, in usec:
 * fft.256
 * Smpl 7208	Wind 700	Revb 748	SplitRR_T 4316	GainR 996	Magnit1 4560	Magnit2 576
 * fft.512
 * Smpl 14384	Wind 1388	Revb 1488	SplitRR_T 9572	GainR 2144	Magnit1 7328	Magnit2 1084
 * 
 * There is two subfunctions for magnitude calculation, as you can see second one runs 
 * about 10x times faster, but it is less accurate, error in worst case scenario
 * may reach 5 %. Approximation based on
 *
 * http://www.dspguru.com/dsp/tricks/magnitude-estimator
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute copies of the Software, 
 * and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY,  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 *
 * Copyright (C) 2014 Anatoly Kuzmenko.
 * All Rights Reserved.
 * 30 Sept. 2014 
 * k_anatoly@hotmail.com
 *********************************************************************************************
 */

#include "SplitRadixRealT.h"

SplitRadixRealT::SplitRadixRealT() {
}

//static inline void SplitRadixRealT::mult_shf_I( int c, int s, int x, int y, int &u, int &v)  __attribute__((always_inline));
inline void SplitRadixRealT::mult_shf_I( int c, int s, int x, int y, int &u, int &v)
{
  u = (mult_shf_s16x16(x, c) - mult_shf_s16x16(y, s));    // Optimizer macro-mulriplier
  v = (mult_shf_s16x16(y, c) + mult_shf_s16x16(x, s));    // Hardcoded >>8 bits, use with 8-bits Sinewave ONLY.
}

//static inline void SplitRadixRealT::sumdiff(int &a, int &b)  __attribute__((always_inline));
inline void SplitRadixRealT::sumdiff(int &a, int &b)
{ int t = a - b; a += b; b = t; }

//static inline void SplitRadixRealT::sumdiff_r(int &a, int &b)  __attribute__((always_inline));
inline void SplitRadixRealT::sumdiff_r(int &a, int &b)
{ int t = b - a; a += b; b = t; }

//static inline void SplitRadixRealT::sumdiff(int a, int b, int &s, int &d)  __attribute__((always_inline));
inline void SplitRadixRealT::sumdiff(int a, int b, int &s, int &d)
{ s = a + b; d = a - b; }

//static inline void SplitRadixRealT::sumdiff3(int &a, int b, int &d)  __attribute__((always_inline));
inline void SplitRadixRealT::sumdiff3(int &a, int b, int &d)
{ d = a - b; a += b; }

//static inline void SplitRadixRealT::diffsum3_r(int a, int &b, int &s)  __attribute__((always_inline));
inline void SplitRadixRealT::diffsum3_r(int a, int &b, int &s)
{ s = a + b; b -= a; }


void SplitRadixRealT::fft_split_radix_real( int *x, int ldn)
{
  const uint16_t n = (1UL << ldn);
  int * fini = x + n;

  int  id = 4;
  for (uint16_t ix = 0;  ix < n;)
  {
   for ( int * i0 = x + ix; i0 < fini; i0 += id)
       sumdiff( i0[0], i0[1]);
   ix = 2 * (id - 1);
   id *= 4;
  }

  uint16_t n2 = 2;
  uint16_t nn = n >> 1;
  while ( nn >>= 1 )
  {
        n2 <<= 1;
        uint16_t id = n2 << 1;
        uint8_t n4  = n2 >> 2; // 8-b
        uint8_t n8  = n2 >> 3;

        uint8_t e  = NWAVE / n2;

        uint16_t ix = 0;
        do
        {
            for ( int * i0 = x + ix; i0 < fini; i0 += id)
            {
                int * i1 = i0;
                int * i2 = i1 + n4;
                int * i3 = i2 + n4;
                int * i4 = i3 + n4;

          int t1;
                diffsum3_r((*i3), (*i4), t1);
                sumdiff3((*i1), t1, (*i3));

                if ( n4 != 1 )
                {
                    i1 += n8;
                    i2 += n8;
                    i3 += n8;
                    i4 += n8;

              int t2;
                    sumdiff((*i3), (*i4), t1, t2);
                    t1 = mult_shf_s16x16( -t1, 181);
                    t2 = mult_shf_s16x16(  t2, 181);
                    sumdiff(t1, (*i2), (*i4), (*i3));
                    sumdiff3((*i1), t2, (*i2));
                }
            }
        ix = (id << 1) - n2;
        id <<= 2;
        }   while ( ix < n );

        if ( n8 > 1 ) { // Optimization
            ix = 0;
            id = n2 << 1;
            do {
                for ( int * i0 = x + ix; i0 < fini; i0 += id) {
                    for (uint8_t j = 1; j < n8; j++) {
                         uint8_t a = j * e;
                         int cc1, ss1, cc3, ss3;
                            ss1 = pgm_read_word(&Sinewave[    a]);
                            cc1 = pgm_read_word(&Sinewave[    a + NQUAT]);
                            ss3 = pgm_read_word(&Sinewave[3 * a]);
                            cc3 = pgm_read_word(&Sinewave[3 * a + NQUAT]);
		            int * i1 = i0 + j;
		            int * i2 = i1 + n4;
		            int * i3 = i2 + n4;
		            int * i4 = i3 + n4;
		            int * i5 = i0 + n4 - j;
		            int * i6 = i5 + n4;
		            int * i7 = i6 + n4;
		            int * i8 = i7 + n4;
		            int t1, t2;
	                          mult_shf_I(cc1, ss1, (*i7), (*i3), t2, t1);
	                    int t3, t4;
	                          mult_shf_I(cc3, ss3, (*i8), (*i4), t4, t3);
	                          sumdiff(t2, t4);
	                          sumdiff(t2, (*i6), (*i8), (*i3));
	                          sumdiff_r(t1, t3);
	                          sumdiff(t3, (*i2), (*i4), (*i7));
	                          sumdiff3((*i1), t1, (*i6));
	                          diffsum3_r(t4, (*i5), (*i2));
	                    }
	                }
            ix = (id << 1) - n2;
            id <<= 2;
            }   while ( ix < n );
        }
    }
}

void SplitRadixRealT::rev_bin( int *fr, int fft_n)
{
    int m, mr, nn, l;
    int tr;

    mr = 0;
    nn = fft_n - 1;

    for (m=1; m<=nn; ++m) {
            l = fft_n;
         do {
             l >>= 1;
            } while (mr+l > nn);

            mr = (mr & (l-1)) + l;

        if (mr <= m)
             continue;
            tr = fr[m];
            fr[m] = fr[mr];
            fr[mr] = tr;
    }
}

void SplitRadixRealT::get_Magnit1(int *fr)
{	
   for (int  i = 1; i < MIRROR; i++) {
        int real = fr[i];
        int imag = fr[FFT_SIZE -i];
        int Magnit = (int) (sqrt(((long)real * real) + ((long)imag * imag)) + 0.5);
        fr[i] = Magnit;
     }
}

void SplitRadixRealT::get_Magnit2(int *fr)
{	
   const int16_t  alpha =  243, beta = 100;   
   for (int  i = 1; i < MIRROR; i++) {
      int tmp_M;
      int abs_R = abs(fr[i]);
      int abs_I = abs(fr[FFT_SIZE -i]);

      if (abs_R > abs_I) tmp_M = mult_shf_s16x16( alpha, abs_R) + mult_shf_s16x16( beta, abs_I);
      else               tmp_M = mult_shf_s16x16( alpha, abs_I) + mult_shf_s16x16( beta, abs_R);

      fr[i] = tmp_M;
     }
}

void SplitRadixRealT::gain_Reset(int *fr, int r_bit)
{
    for ( int  i = 0; i < FFT_SIZE; i++) {
        int delit = fr[i];
        if ( delit  <  0 ) delit = ((delit >> r_bit) +1); 
        else delit = delit >> r_bit;
        fr[i] = delit;
    }
}

