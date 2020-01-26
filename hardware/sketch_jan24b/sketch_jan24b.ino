int averageMoisture[5];
int i = 0;
int total;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  total = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  //averageMoisture[i++] = analogRead(A0);
  //total += averageMoisture[i-1];
  total = analogRead(A0);
  //if (i >= sizeof(averageMoisture)) {
    //i = 0;
    if (total > 700) {///sizeof(averageMoisture) > 400) {
      Serial.println(1);
      total = 0;
    } else {
      Serial.println(0);
      total = 0;
    }
  //}
}
