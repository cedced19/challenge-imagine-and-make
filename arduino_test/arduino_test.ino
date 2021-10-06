
int rPot;
int bPot;

void setup()
{
  Serial.begin(9600); //com speed. bits per second
  pinMode(9, OUTPUT);
  pinMode(2, INPUT_PULLUP); //add pullup resistor
}

void loop(){
  rPot = analogRead(0);
  bPot = analogRead(1);
  Serial.print("R = ");
  Serial.print(rPot);
  Serial.print(" B = ");
  Serial.println(bPot);
  if( !digitalRead(2) || rPot<315 || rPot>715 || bPot<315 || bPot>715) {
	digitalWrite(9, HIGH);
  } else {
	digitalWrite(9, LOW);
  }
  delay(200);
}