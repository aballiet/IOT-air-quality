#include "DHTesp.h"
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define DHTpin 14    //D5 of NodeMCU is GPIO14
#define LED_CTRL  D8

const char* ssid     = "";
const char* password = "";
const char* API_KEY  = "";
const int delay_post = 600000; // each 10 minutes

// On instancie un client HTTP qui lancera la requete
HTTPClient oThinkSpeakClient;
DHTesp dht;

void setup()
{
  Serial.begin(115200);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print("Connecting..");
  }

  // LED de controle 
  pinMode( LED_CTRL, OUTPUT );
  digitalWrite( D1, LOW) ; //On allumera la LED quand on enverra des données.

  dht.setup(DHTpin, DHTesp::DHT11); //for DHT11 Connect DHT sensor to GPIO 17
}

void loop(){
  
  if (WiFi.status() == WL_CONNECTED) { 
 
    HTTPClient http;

    //Light Up the LED
    Serial.println( "\n Measuring..." );
    digitalWrite( LED_CTRL, HIGH );

    float humidity = dht.getHumidity();
    float temperature = dht.getTemperature();

    Serial.print("Temperature = ");
    Serial.print(temperature);
    Serial.print("Humidity = ");
    Serial.println(humidity);
    delay(1);

    // Send measures to ThingSpeak
    int res = sendThingSpeak(humidity, temperature);
    switch (res){
      case 0 :
        // L'appel de la fonction c'est bien passé
        Serial.println("OK");
        break;
       default :
        Serial.println("Failed");
        break;
    }
  delay(delay_post);
  }
}

int sendThingSpeak(float field1, float field2){
  int res = 0;
  
  String osUrl = "http://api.thingspeak.com";

  osUrl += "/update?api_key=";
  osUrl += API_KEY;
  osUrl += "&field1=" + String(field1);
  osUrl += "&field2=" + String(field2);

  Serial.print("Sending to: "); 
  Serial.println(osUrl);

  oThinkSpeakClient.begin(osUrl);
  int iHttpCode = oThinkSpeakClient.GET();
  if ( iHttpCode ){
    if ( iHttpCode != 200 ){
      String osPayload = oThinkSpeakClient.getString();
      Serial.println( "oThinkSpeakClient response error " );
      Serial.println( osPayload );
      Serial.print( "iHttpCode : " );
      Serial.println( iHttpCode );
      res = 1;
    }
  } else {
    Serial.println( "oThinkSpeakClient not response" );
    res = 2;
   }
  oThinkSpeakClient.end();
  
  return res;
 }
