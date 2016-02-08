#define LED 13
//#define Sounder 10
#define Button 7

int key=0;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(Button,INPUT_PULLUP);
}

void loop() {
  key=digitalRead(Button);
  
  if (key == LOW) {
    digitalWrite(LED,HIGH);
    tone(10,1000,10);
  }
  else {
    digitalWrite(LED,LOW);
  }

} 
