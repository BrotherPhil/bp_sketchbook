#define DIRECTION 2
#define MAGNITUDE 3

void setup() {
    Serial.begin(57600);
    pinMode(DIRECTION, OUTPUT);
    pinMode(MAGNITUDE, OUTPUT);
}

void loop() {
    int x = Serial.read();
    if (x == -1)
        return;

    if (x < 128) {
        digitalWrite(DIRECTION, LOW);
        analogWrite (MAGNITUDE, 2*(127 - x));
    } else {
        digitalWrite(DIRECTION, HIGH);
        analogWrite (MAGNITUDE, 255 - 2*(x - 128));
    }
}

