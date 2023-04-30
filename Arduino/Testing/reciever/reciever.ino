#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN   9
#define CSN_PIN 10
#define LED 4

const byte thisSlaveAddress[6] = "00001";

RF24 radio(CE_PIN, CSN_PIN);

//===========

void setup() {

    Serial.begin(9600);

    Serial.println("SimpleRx Starting");

    pinMode(LED, OUTPUT);
    
    radio.begin();
    radio.setAutoAck(false);
    radio.setDataRate( RF24_250KBPS );
    radio.setChannel(100);
    radio.setPALevel(RF24_PA_HIGH);
    radio.openReadingPipe(0, thisSlaveAddress);
    radio.startListening();
}

//=============

void loop() 
{
  if (radio.available())
  {
    int r_data;
    radio.read(&r_data, sizeof(r_data));
    Serial.println(r_data);

    switch (r_data)
    {
      case 1:
      digitalWrite(LED, HIGH);
      delay(100);
      break;

      case 0:
      digitalWrite(LED, LOW);
      delay(100);
      break;
    }
  }
}
