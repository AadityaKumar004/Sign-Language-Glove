int flexpin0 = A0;
int flexpin1 = A1;
int flexpin2 = A2;
int flexpin3 = A3;
int flexpin4 = A4;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int flexVal0;
  int flexVal1;
  int flexVal2;
  int flexVal3;
  int flexVal4;
  flexVal0 = analogRead(flexpin0);
  flexVal1 = analogRead(flexpin1);
  flexVal2 = analogRead(flexpin2);
  flexVal3 = analogRead(flexpin3);
  flexVal4 = analogRead(flexpin4);
  
  Serial.print(flexVal0);
  Serial.print(",");
  Serial.print(flexVal1);
  Serial.print(",");
  Serial.print(flexVal2);
  Serial.print(",");
  Serial.print(flexVal3);
  Serial.print(",");
  Serial.println(flexVal4);
  delay(800);
}
