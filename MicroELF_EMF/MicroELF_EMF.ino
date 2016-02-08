/*
 
	MicroELF_EMF: Electrical radiation measurement
	Revision 03

	Applicable license :

	This program and related documentation are owned by HL2 group SAS. 
	The program is subject to the license GNU GPL version 3. This license 
	allows you to use, reproduce and adapt this program for private, 
	educational, research purposes. 
	
*/
/ http://www.smokeandwires.co.nz
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

#include <PlainDSP.h>

/* Create objects */
PlainDSP DSP;

const uint8_t ctrlLedMask = (1 << PINB5);

/* Acquisition parameters */
const uint16_t _samples = 128; /* Max value depends upon available memory space */
const float _samplingFrequency = 400.0; /* From 0.125 Hz to 80 kHz */
const uint16_t _adcChannel = 5; /* From 0 to 5 on ATmega328 powered Arduino */
const uint16_t _refVoltage = DSP_REF_VOL_INTERNAL; /* Internal: 1.1V */
const uint8_t _options = (DSP_OPT_DIS_TIM_0 | DSP_OPT_DIS_TIM_2 | DSP_OPT_NOI_CANCELLER);
/* Display parameters */
const float _targetFrequency = 50.0;
const float _frequencyTolerance = 5.0;
const uint16_t _maxOnTime = 600;

void setup(void)
{
	/* Initialize serial comm port */
	Serial.begin(115200); 
	/* Set data acquisition parameters */
	DSP.SetAcquisitionEngine(_adcChannel, _refVoltage,  _samplingFrequency, _samples, _options);
	/* Init control LED */
	DDRB |= ctrlLedMask;
        tft.fillScreen(BLACK);
        tft.fillScreen(RED);
        tft.fillScreen(GREEN);
        tft.fillScreen(BLUE);
        tft.fillScreen(BLACK);
        tft.setCursor(0,0);
        tft.setTextColor(GREEN); 
        tft.setTextSize(3);
        tft.setTextColor(RED); 
        tft.print("E");
        tft.setTextColor(WHITE); 
        tft.print("L");
        tft.setTextColor(BLUE); 
        tft.print("F");
        tft.setTextColor(MAGENTA); 
        tft.println(" Detector");
        tft.setTextColor(GREEN); 
       
}


void loop(void)
{
	/* Acquire data from selected channel */
	DSP.GetScanData(); 
	/* Null offset */
	DSP.ResetOffset();
	/* Weight data */
	DSP.Windowing(DSP_WIN_TYP_HANN, DSP_FORWARD);	
	/* Compute FFT */
	DSP.ComputeForwardFFT();	
	/* Compute amplitudes */
	DSP.ComplexToReal(DSP_SCL_TYP_AMPLITUDE);
	/* Find target peak */
	struct strPeakProperties targetPeak;
	DSP.TargetPeak(_targetFrequency, _frequencyTolerance, &targetPeak);
	/* Compute blink on/off ratio */
	uint16_t onTime = uint16_t(targetPeak.height);
	if (onTime > _maxOnTime) {
		onTime = _maxOnTime;
	}	
	uint16_t offTime = (_maxOnTime - onTime);
	/* Control LED */
	PORTB |= ctrlLedMask; /* Toggle control led on */
	delay(onTime);
	PORTB &= ~ctrlLedMask; /* Toggle control led off */
	delay(offTime);
	/* Optionally print data */
        tft.setCursor(0,2);
        tft.print((millis() / 1000.0), 3);
	tft.print(';');
	tft.print(targetPeak.height, 2);
	tft.println();
}
