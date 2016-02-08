#define Blue 13
#define Green 11
#define Red 12
#define Sounder 9
#define Button_long 7
#define Button_short 8

int val_long=0;
int val_short=0;

void setup() {
  pinMode(Red,OUTPUT);
  pinMode(Green,OUTPUT);
  pinMode(Blue,OUTPUT);
  pinMode(Button_short,INPUT);
  pinMode(Button_long,INPUT);
}

void loop() {
  val_long=digitalRead(Button_long);
  
  if (val_long == HIGH) {
    digitalWrite(Red,HIGH);
    delay (200);
    digitalWrite(Red,LOW);
    tone(9,262,750);
    digitalWrite(Green,HIGH);
    delay (50);
    digitalWrite(Green,LOW);
  }
  else {
    digitalWrite(Red,LOW);
  }
  
  val_short=digitalRead(Button_short);
  
  if (val_short == HIGH) {
    digitalWrite(Blue,HIGH);
    delay (200);
    digitalWrite(Blue,LOW);
    tone(9,262,250);
    digitalWrite(Green,HIGH);
    delay (50);
    digitalWrite(Green,LOW);
  }
  else {
    digitalWrite(Blue,LOW);
  }
  
} 
