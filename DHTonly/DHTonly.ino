  #include "DHT.h"
#define dhtPin 8      //讀取DHT11 Data
#define dhtType DHT11 //選用DHT11  
int redPin = 9;
int greenPin = 10;
int bluePin = 11;

DHT dht(dhtPin, dhtType); // Initialize DHT sensor

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT); 
  Serial.begin(9600);//設定鮑率9600
  dht.begin();//啟動DHT
}

void loop() {
  float h = dht.readHumidity();//讀取濕度
  float t = dht.readTemperature();//讀取攝氏溫度
  float f = dht.readTemperature(true);//讀取華氏溫度
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("無法從DHT傳感器讀取！");
    return;
  }
//  Serial.print("濕度: ");
  Serial.print(h);
  Serial.print("\t");
//  Serial.print("攝氏溫度: ");
  Serial.print(t);
  Serial.print("\t");
//  Serial.print("華氏溫度: ");
  Serial.print(f);
  Serial.print("\n");
  if(t==33){
    setColor(255, 0, 0);  // red

  }
  else if(t==32){
    setColor(255, 255, 0);  // yellow

  }
  else if(t==31){
    setColor(0, 255, 0);  // green

  }
  else if(t==30){
    setColor(0, 0, 255);  // blue

  }
  else if(t==29){
    setColor(80, 0, 80);  // purple

  }
  else if(t==28){
    setColor(0, 255, 255);  // aqua

  }
  else if(t==27){
    setColor(255, 0, 255);

  }
  else if(t==26){
    setColor(80, 80, 0);

  }
  else if(t==25){
    setColor(0, 80, 80);

  }
  delay(5000);//延時5秒
}

void setColor(int red, int green, int blue)
{
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}
