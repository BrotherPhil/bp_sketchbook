#define LED 13
#define Sounder 11 // Connect to Speaker / left ear for sidetone and 3.5mm ring (red) for MCW
#define Button 7 // Connect to button or Straight key
#define Xmit 10 // Connect to 3.5mm shield (clear)
// Connect 2.5mm shield/ring (blue) to gnd, and 2.5mm tip to right ear. 
unsigned long XmitRunOn = 500; // Transmit delay before opening key - default to 1/2 second
unsigned long XmitTimeout = 600000; // Transmit timeout - default to 10 minutes
unsigned long timer0;

int key=0;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(Button,INPUT_PULLUP);
  pinMode(Xmit,OUTPUT);
  digitalWrite(Xmit,LOW);
  timer0 = millis(); // reset timer
}

void loop() {
  key=digitalRead(Button);
  
  if (key == LOW) {
    digitalWrite(LED,HIGH);
    digitalWrite(Xmit,LOW);
    timer0 = millis(); // reset timer
    tone(Sounder,1000,10);
  }
  else {
    if ((millis()-timer0) > XmitRunOn) {
      digitalWrite(LED,LOW);
      digitalWrite(Xmit,HIGH);
    timer0 = millis(); // reset timer
    }
  }
  if ((millis()-timer0) > XmitTimeout) { // Ooops! Transmitted for too long!
    digitalWrite(LED,LOW);
    digitalWrite(Xmit,HIGH);
  timer0 = millis(); // reset timer
  delay(300000); // Force a timeout to let the transmitter cool down - default to 5 minutes.
  }

} 
