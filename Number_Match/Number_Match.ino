
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

int digit[10]={1,5,2,9,3,0,5,9,6,7};
int match[10]={0,0,0,0,0,0,0,0,0,0};
int lock[10]={0,0,0,0,0,0,0,0,0,0};
String diala="";
String dialb="";
int count=0;
int i=0;
int r=0;

void setup()                   
{
    // set up the LCD's number of columns and rows: 
    lcd.begin(16, 2);
    // Seed random number generator from (hopefully) floating ADC input
    randomSeed(analogRead(0));
}

void loop()                     // run over and over again
{
  int lock[10]={0,0,0,0,0,0,0,0,0,0};

  while(count<10)
  { 
    count=0;
    diala="0(";
    dialb="0(";
    for (i=0; i<10; i=i+1)
    {
        if(lock[i]==0)    
        {
            match[i]=random(10);
        }
        if(match[i]==digit[i])
        {
          if (lock[i]==0)
          {
            r=random(10);
            if (r==0)
            {
              count=count+1;
              lock[i]=1;
            }
          }
        }
        diala=diala+char(match[i]+48);
        if (lock[i]==1)
         {
           dialb=dialb+char(digit[i]+48);
         }
         else
         {
           dialb=dialb+" ";
         } 

         if (i==2)
         {
           diala=diala+")";
           dialb=dialb+")";
         }
         if (i==5)
         {
           diala=diala+"-";
           dialb=dialb+"-";
         }
           
    }
    lcd.setCursor(0,0);
    lcd.print(diala);
//    lcd.printf("(%2d)",count);
    lcd.setCursor(0,1);
    lcd.print(dialb);
    delay(200);
  }
    for (i=0; i<5; i=i+1)
    {
      lcd.noDisplay();
      delay(500);
      lcd.display();
      delay(500);
    }
    lcd.clear();
}
  
 
    
        


 

