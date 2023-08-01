#include <SoftwareSerial.h>
SoftwareSerial hc12(7,8); // Rx,Tx

int led=13,data;
int pin1=2,pin2=3;
int pin3=4,pin4=5; 

// mesure de la distance, pour eviter les obstacles

//int trigger=7;
//int echo=8;

int v1=5,v2=6;//Vitesse moteur1,Vitesse moteur2

void setup() {

//obstacles

//pinMode(trigger,OUTPUT);
//pinMode(echo,INPUT);

// signalisation  
pinMode(led,OUTPUT);

//moteur1
pinMode(pin1,OUTPUT);
pinMode(pin2,OUTPUT);

//moteur2
pinMode(pin3,OUTPUT);
pinMode(pin4,OUTPUT);

hc12.begin(9600);
Serial.begin(9600);
}
void loop() {

if(hc12.available()!=0){
  data=hc12.read();
  digitalWrite(led,HIGH);
  delay(400);
  digitalWrite(led,LOW);
  delay(400);
}

//Car Orientation 2 

if(data=='1'){   // Forward
  digitalWrite(pin1,HIGH);
  digitalWrite(pin3,HIGH);
    
}
else if(data=='2'){   //Behind
  digitalWrite(pin1,LOW);
  analogWrite(pin2,255);
  digitalWrite(pin3,LOW);
  analogWrite(pin4,255);
  }
else if(data=='3'){   //Right
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,LOW);
  //digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  }

else if(data=='4'){   //Left
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,HIGH);
  //digitalWrite(pin4,LOW);
  }


//car objects skipper

//digitalWrite(trigger,LOW);
//delay(3);
//digitalWrite(trigger,HIGH);
//delay(5);
//digitalWrite(trigger,LOW);
//
//int duree=pulseIn(echo,HIGH);
//int t=duree/1000/1000/2;
//int distance=340*t*100; //distance in Cm
//
//if (distance<=10){
//  digitalWrite(pin2,HIGH);
//  digitalWrite(pin4,HIGH);
//}

}
