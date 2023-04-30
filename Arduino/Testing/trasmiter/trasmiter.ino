#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


#define CE_PIN   9
#define CSN_PIN 10

const byte slaveAddress[6] = "00001";


RF24 radio(CE_PIN, CSN_PIN); // Create a Radio

void setup() {

    Serial.begin(9600);

    Serial.println("SimpleTx Starting");

    radio.begin();
    radio.setAutoAck(false);
    radio.setDataRate( RF24_250KBPS );
    radio.setPALevel(RF24_PA_HIGH);
    radio.setChannel(100);
    radio.openWritingPipe(slaveAddress);
    radio.stopListening();
}

//====================

void loop() 
{
  //int input = Serial.read();
  Send(1);
  delay(100);
  Send(0);
  delay(100);
}

void Send(int send_data)//fungsi untuk mengirim sinyal radio ke reciever
{
  radio.write(&send_data, sizeof(send_data));
}
