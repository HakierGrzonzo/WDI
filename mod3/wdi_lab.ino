const int ledCount = 7;

int ledPins[] = {
  6, 7, 8, 9, 10, 11, 12
};   // an array of pin numbers to which LEDs are attached


void setup() {
  pinMode(A0, INPUT);
  // loop over the pin array and set them all to output:
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    pinMode(ledPins[thisLed], OUTPUT);
  }

  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(A0));

  int ledLevel = map(analogRead(A0), 0, 1019, 0, ledCount);

  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    if (thisLed < ledLevel) {
      digitalWrite(ledPins[thisLed], HIGH);
    } else {
      digitalWrite(ledPins[thisLed], LOW);
    }
  }
}
