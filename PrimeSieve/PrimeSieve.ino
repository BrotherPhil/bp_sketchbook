/*
 * PrimeSieve
 * Paul Badger 2009
 * Generates prime numbers less than 63,001 as shown
 * To extend just add more primes to prime table (and choose a larger data type)
 * The program will generate primes up to the square of the last prime table entry

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

// just add more primes to the prime table for larger search
// byte data type to save memory - use a larger datatype with prime table entries above 255 :)
byte primes[]={ 
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
    102, 107, 109, 113, 127, 131,  137 , 139, 149, 151, 157, 163, 167, 173,  179, 181, 191, 193, 197, 
    199, 211, 223, 227, 229, 233, 239, 241, 251 };

// if you change the datatype of primes array to int, change next line to 
// "const int TopPrimeIndex = (sizeof(primes)/2) - 1;"

const unsigned int TopPrimeIndex = sizeof(primes) - 1;      
const unsigned long TopPrimeSquared = (long)primes[TopPrimeIndex] * (long)primes[TopPrimeIndex];
int primeFlag;


void setup()                   
{
    // set up the LCD's number of columns and rows: 
    lcd.begin(16, 2);

 
    lcd.print("Number of primes in prime table = ");
    lcd.println(TopPrimeIndex);
  
    lcd.print("Last prime in table =  ");
    lcd.println((unsigned int)primes[TopPrimeIndex]);
 

    lcd.print("Calculating primes through ");
    lcd.println(TopPrimeSquared);
    

}
void loop()                     // run over and over again
{
    for (long x = 1; x < TopPrimeSquared; x+=2){  // skips even numbers, including 2, which is prime, but it makes algorithm tad faster

            for (long j=0; j < TopPrimeIndex; j++){
            primeFlag = true;

            if (x == primes[j]) break;

            if (x % primes[j] == 0){     // if the test number modolo (next number from prime table) == 0 
                primeFlag = false;       //  then test number is not prime, bailout and check the next number
                break;
            }
        }
        if (primeFlag == true){           // found a prime - print it
            lcd.println(x);
       }
    }
}


