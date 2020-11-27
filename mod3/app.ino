void setup() {
  // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
    // read the input on analog pin 0:
    int sensorValue = analogRead(A0) / 4;
    // print out the value you read:
    for (int i = 2; i < 10; i++)
    {
        if (sensorValue % 2 == 1)
            digitalWrite(i, HIGH);
        else
            digitalWrite(i, LOW);
        sensorValue = sensorValue >> 1;
    }
}