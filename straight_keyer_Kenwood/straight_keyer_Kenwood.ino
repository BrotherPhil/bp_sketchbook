#define LED 13
#define Sounder 11 // Connect to Speaker / left ear for sidetone and 3.5mm ring
#define Button 7 // Connect to button or Straight key
#define Xmit 10 // Connect to 3.5mm shield
// Connect 2.5mm shield/ring to gnd, and 2.5mm tip to right ear. 
unsigned long XmitTimeout = 1000 // Transmit delay before opening key
unsigned long timer0;

int key=0;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(Button,INPUT_PULLUP);
  pinMode(Xmit,OUTPUT);
  digitalWrite(Xmit,LOW);
}

void loop() {
  key=digitalRead(Button);
  
  if (key == LOW) {
    digitalWrite(LED,HIGH);
    digitalWrite(Xmit,LOW);
    timer0 = millis(); // tart 
    tone(Sounder,1000,10);
  }
  else {
    if (timer0 > XmitTimeout) {
      digitalWrite(LED,LOW);
      digitalWrite(Xmit,HIGH);
    }
  }

} 
