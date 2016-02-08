// Cal-Eng 4-digit LEDuino/Robosapien walking routine.


// Define the LED digit segment patterns, from 0 - 9
// Array below defines segment on/off for digits 0-9 as segment A,B,C,D,E,F,G
// Zero represent an ON state (common anode)  
// Note: Decimal point is pin A4

//                  Arduino pins: 10,9,8,7,6,5,4
byte seven_seg_digits[10][7] = { { 0,0,0,0,0,0,1 },  // = 0
                                 { 1,0,0,1,1,1,1 },  // = 1
                                 { 0,0,1,0,0,1,0 },  // = 2
                                 { 0,0,0,0,1,1,0 },  // = 3
                                 { 1,0,0,1,1,0,0 },  // = 4
                                 { 0,1,0,0,1,0,0 },  // = 5
                                 { 0,1,0,0,0,0,0 },  // = 6
                                 { 0,0,0,1,1,1,1 },  // = 7
                                 { 0,0,0,0,0,0,0 },  // = 8
                                 { 0,0,0,1,1,0,0 }   // = 9
                                                           };
                                                           
                                                           
                                                   

const int irPin = 2;
const int tsDelay = 833; // us, as estimated
// const int tsDelay = 1666; // us, as estimated 8MHz


int allowWalkForward = 1;
int allowTurnLeft = 1;
int sensorValueSideOld = 0;

int sensorValueFront = 0;
int sensorValueSide = 0;



enum roboCommand {
  // only a very small subset of commands
  turnRight = 0x80,
  rightArmUp = 0x81,
  rightArmOut = 0x82,
  tiltBodyRight = 0x83,
  rightArmDown = 0x84,
  rightArmIn = 0x85,
  walkForward = 0x86,
  walkBackward = 0x87,
  turnLeft = 0x88,
  leftArmUp = 0x89,
  leftArmOut = 0x8A,
  tiltBodyLeft = 0x8B,
  leftArmDown = 0x8C,
  leftArmIn = 0x8D,
  stopMoving = 0x8E,
   
  // noises
  whistle = 0xCA,
  roar = 0xCE,
  burp = 0xC2 
};

                                                       

void setup() {  


 TIMSK1 = bit(TOIE1); //overflow interrupt enable
 
  pinMode(irPin, OUTPUT);
  digitalWrite(irPin, HIGH); 

pinMode(10, OUTPUT);  
pinMode(9, OUTPUT);  
pinMode(8, OUTPUT); 
pinMode(7, OUTPUT);  
pinMode(6, OUTPUT);  
pinMode(5, OUTPUT);   
pinMode(4, OUTPUT);

pinMode(A4, OUTPUT);

pinMode(A0, OUTPUT);
pinMode(A1, OUTPUT);
pinMode(A2, OUTPUT);
pinMode(A3, OUTPUT);

pinMode(13, OUTPUT);


blankLED();

decimalPointOn(1);  // start with the decimal point off


  sevenSegClear();
  
  delay(1000); 
  writeCommand(burp);
     
  delay(3000); 
  writeCommand(walkForward);
  
  
}



int intValue = 0;
int interruptLED = 0;
int ledDisplayValue = 0;

int countOnes = 0;
int countTens = 0;
int countHund = 0;
int countThou = 0;

int countOnesVal = 0;
int countTensVal = 0;
int countHundVal = 0;
int countThouVal = 0;





void blankLED() {
  
  // This turns OFF the PNP transistors connected to each digit's common-anode line
  digitalWrite(A0, HIGH);   
  digitalWrite(A1, HIGH);   
  digitalWrite(A2, HIGH);   
  digitalWrite(A3, HIGH);
  
}


void decimalPointOn(byte dp) {
  digitalWrite(A4, dp);
}
   
   
void sevenSegWrite(byte digit) {
  byte pin = 10;
  for (byte segCount = 0; segCount < 7; ++segCount) {
    digitalWrite(pin, seven_seg_digits[digit][segCount]);
    --pin;
  }
}



// Timer1 interrupt overflow function.  Called every 1/500 of a second.
// Note: Keep ISR routines as short and as simple as possible
ISR(TIMER1_OVF_vect){

  interruptLED++;
  
  if (interruptLED > 1) {
      intValue++;
      updateDisplay(ledDisplayValue);
  }

}



void updateDisplay(word ledDisplayValue) {

  
        countThou = ledDisplayValue / 1000;
        countThouVal = countThou * 1000;
        
        countHund = (ledDisplayValue - countThouVal) / 100;
        countHundVal = countHund * 100;
        
	countTens = (ledDisplayValue - (countThouVal + countHundVal)) / 10;
        countTensVal = countTens * 10;

	countOnes = ledDisplayValue - (countThouVal + countHundVal + countTensVal);
    

switch (intValue-1) {
  case 0:
    blankLED();
    sevenSegWrite(countOnes);
    digitalWrite(A0, LOW); 
    break;
  case 1:
    blankLED();
    sevenSegWrite(countTens);
    digitalWrite(A1, LOW); 
    break;
  case 2:
    blankLED();
    sevenSegWrite(countHund);
    digitalWrite(A2, LOW); 
    break;
  case 3:
    blankLED();
    sevenSegWrite(countThou);
    digitalWrite(A3, LOW); 
    break;
  } 
  
  
  if (intValue == 4) {intValue = 0;}
  
  interruptLED = 0;
 
  
}




void sevenSegClear() {
  for (byte pin = 4; pin < 11; ++pin) {
    digitalWrite(pin, HIGH);
  }
}


void delayTs(unsigned int slices) {
  delayMicroseconds(tsDelay * slices); 
}


void writeCommand(int cmd) // this is type 'int' not 'roboCommand' due to an Arduino environment annoyance
{
  // preamble
  digitalWrite(irPin, LOW);
  delayTs(8);
    
  for(char b = 7; b>=0; b--) {
    digitalWrite(irPin, HIGH);
    delayTs( (cmd & 1<<b) ? 4 : 1 );
    digitalWrite(irPin, LOW);
    delayTs(1);        
  } 
  
  digitalWrite(irPin, HIGH);
}





// Main program starts here:

void loop() {
  
   
  sensorValueSide = analogRead(A6);
  sensorValueFront = analogRead(A5);
  ledDisplayValue = sensorValueFront;


  if (sensorValueFront < 450) {
    
   digitalWrite(13, HIGH);   
   
  }
  
  else {   
    
   decimalPointOn(0); 
   sensorValueSide = analogRead(A6);
   sensorValueSideOld = sensorValueSide;
   ledDisplayValue = sensorValueSide;
    
   writeCommand(stopMoving);
   delay(1000);
   
   writeCommand(burp);
   digitalWrite(13, LOW);
   delay(1000);  
   
   allowWalkForward = 0;   
   allowTurnLeft = 1;
  
   
   // While test
   while (allowTurnLeft == 1) {
     
     writeCommand(turnLeft);
     delay(1000);
     writeCommand(stopMoving);
     delay(1000);
     
     sensorValueSide = analogRead(A6);
     // LED displays right-hand sensor value
     ledDisplayValue = sensorValueSide;
     
         if ((sensorValueSideOld - 10) > sensorValueSide)  {
         
           allowTurnLeft = 0;
       
         }
         
     sensorValueSideOld = sensorValueSide;
   
   }
   // End while
  
    
   allowWalkForward = 1;   
   allowTurnLeft = 0; 
   decimalPointOn(1);
   writeCommand(stopMoving);
   delay(1000);  
   writeCommand(walkForward);
  
  
  }
  

}
