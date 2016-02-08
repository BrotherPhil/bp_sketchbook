    #include <SoftwareSerial.h>

    SoftwareSerial sim900(2,3);  //2=FONA_TX  3=FONA_RX!!!!!

    void setup() {
     
      Serial.begin(9600);
      sim900.begin(4800);
      Serial.print("start");
      delay(10000);
      sim900.print("AT+CMGF=1\r");
      delay(100);
      sim900.println("AT+CMGS=\"+64211431669\"");
      delay(100);
      sim900.print("test");
      delay(100);
      sim900.println((char)26);
      delay(200);
      Serial.print("DONE");
     
    }
    void loop() {
    }
