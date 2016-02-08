/*

	MicroTLS: tiny light show
	Copyright (C) 2012 Didier Longueville

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.

*/

#include 
#include 
PlainADC PADC; /* Create ADC object */
PlainFFT FFT; /* Create FFT object */
/* Constants */
#define SCL_INDEX 0x00
#define SCL_TIME 0x01
#define SCL_FREQUENCY 0x02
/* Data acquisition parameters */
const uint16_t samples = 64;
const double samplingFrequency = 16.0E+3;
const uint16_t adcChannel = 0; /* From 0 to 5 on ATmega328 powered Arduinos */
const uint16_t refVoltage = ADC_REF_VOL_DEFAULT; /* VCC: 5V */
/* Data acquisition vector */
uint8_t *vBuffer;
/**/
const uint16_t leds = 6;
const double triggerLevel = 10.0;
/* FFT vectors */
double *vReal;
double *vImag;

void setup() 
{ 
	Serial.begin(115200);
	/* Set data acquisition parameters */
	vBuffer = PADC.SetAcquisitionEngine(adcChannel, refVoltage,  samplingFrequency, samples, ADC_DAT_FMT_DBL);	
	/* Size data vectors */
	vReal = (double*)malloc(samples * sizeof(double));
	vImag = (double*)malloc(samples * sizeof(double));
	/* Set output ports */
	DDRD |= (1 << PIND7);
	DDRB |= ((1 << PINB0) | (1 << PINB1) | (1 << PINB2) | (1 << PINB3) | (1 << PINB4) | (1 << PINB5));
	for (uint8_t i = 0; i < leds; i++) { 
		PORTB |= (1 << i);
		delay(500);
		PORTB &= ~(1 << i);
	}
	for (uint8_t i = 0; i < 6; i++) { 
		PORTB ^= ((1 << PINB0) | (1 << PINB1) | (1 << PINB2) | (1 << PINB3) | (1 << PINB4) | (1 << PINB5));
		delay(500);
	}
	// blinkLed(3, 400);
};

void loop() 
{	
	/* Mark event: flicker led */
	PORTD ^= (1 << PIND7);
	/* Acquire data */
	PADC.GetScanData();
	/* Cast data in a doubles vector */
	vReal = reinterpret_cast(vBuffer);
	/* Suppress data offset */
	FFT.SuppressOffset(vReal, samples);
	/* Clear imaginary vector */
	FFT.ClearVector(vImag, samples);
	/* Optional */
	// PrintVector(vReal, samples, SCL_TIME);
	/* Window data: optional */
	FFT.Windowing(vReal, samples, FFT_WIN_TYP_HAMMING, FFT_FORWARD);	
	/* Compute FFT */
	FFT.Compute(vReal, vImag, samples, FFT_FORWARD);	
	/* Compute magnitudes */
	FFT.ComplexToReal(vReal, vImag, samples, FFT_SCL_TYP_AMPLITUDE);
	/* Normalize data */
	FFT.Normalize(vReal, (samples >> 1), 100.0);
	/* Optional */
	// PrintVector(vReal, (samples >> 1), SCL_FREQUENCY);
	// PlotVector(vReal, (samples >> 1), SCL_FREQUENCY);
	/* And now the show must start ! */
	uint16_t samplesPerLed = uint16_t((samples >> 1) / leds);
	for (uint16_t i = 0; i < leds; i++) {
		double sum = 0.0;
		for (uint16_t j = 0; j < samplesPerLed; j++) {
			sum += vReal[(i * samplesPerLed) + j];
		}
		double average = (sum / samplesPerLed);
		if (average > triggerLevel) {
			PORTB |= (1 << i);
		} 
		else {
			PORTB &= ~(1 << i);
		}
	}
};

void PrintVector(double *vData, uint8_t bufferSize, uint8_t scaleType) 
{	
	for (uint16_t i = 0; i < bufferSize; i++) {
		double abscissa;
		/* Print abscissa value */
		switch (scaleType) {
		case SCL_INDEX:
			abscissa = double(i);
			break;
		case SCL_TIME:
			abscissa = (i / samplingFrequency);
			break;
		case SCL_FREQUENCY:
			abscissa = ((i * samplingFrequency) / samples);
			break;
		}
		Serial.print(abscissa, 6);
		Serial.print("t");
		Serial.print(vData[i], 4);
		Serial.println();
	}
	Serial.println();
};

void PlotVector(double *vData, uint8_t bufferSize, uint8_t scaleType) 
{	
	for (uint16_t i = 0; i < bufferSize; i++) {
		double abscissa;
		/* Print abscissa value */
		switch (scaleType) {
		case SCL_INDEX:
			abscissa = double(i);
			break;
		case SCL_TIME:
			abscissa = (i / samplingFrequency);
			break;
		case SCL_FREQUENCY:
			abscissa = ((i * samplingFrequency) / samples);
			break;
		}
		Serial.print(abscissa, 1);
		Serial.print("t");
		uint8_t ordinate = vData[i];
		ordinate >>= 2;
		for (uint8_t j = 0; j < ordinate; j++) {
			Serial.print('X');
		}
		Serial.println();
	}
	Serial.println();
};

void blinkLed(uint16_t cycles, uint16_t duration) 
/* Blink control led */
{
	/* Reset pin state */
	PORTD &= ~(1 << PIND7); /* Turn control led off */
	for (uint8_t i = 0; i < (cycles << 1); i++)	{
		delay(duration >> 1);
		PORTD ^= (1 << PIND7);
	}
};
