#include <SoftwareSerial.h>
 
SoftwareSerial hc12(10,11); // Rx,Tx
int data;

void setup() {
  
hc12.begin(9600);
Serial.begin(9600);
}
void loop() {
  
if(Serial.available()!=0){
  data=Serial.read();
  }  
if(Serial.available()!=0){
  hc12.write(data);
  }
}
