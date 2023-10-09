int redLedPin = 9;   // Connect red LED to digital pin 9
int blueLedPin = 10;  // Connect blue LED to digital pin 10
void setup() {
  Serial.begin(9600);
  pinMode(redLedPin, OUTPUT);
  pinMode(blueLedPin, OUTPUT);
}
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'R') {
      digitalWrite(redLedPin, HIGH);   // Turn on red LED
      digitalWrite(blueLedPin, LOW);   // Turn off blue LED
    } else if (command == 'B') {
      digitalWrite(redLedPin, LOW);    // Turn off red LED
      digitalWrite(blueLedPin, HIGH);  // Turn on blue LED
    }
  }
}