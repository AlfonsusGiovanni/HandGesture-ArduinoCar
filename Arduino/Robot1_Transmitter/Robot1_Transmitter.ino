#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN   9
#define CSN_PIN 10

const byte address[6] = "00001"; // Alamat komunikasi
RF24 radio(CE_PIN, CSN_PIN); // Inialisasi pin CE dan CSN pada nRF24L01

// Data dari python
int python_data;

/////////////////////////////////////////////////////////////

void setup() 
{
  Serial.begin(9600);
  Serial.setTimeout(10); 

  Serial.println("TX STARTING");

  //setup transmiter nrf240L1
  radio.begin();
  radio.setAutoAck(false);
  radio.setDataRate(RF24_250KBPS);
  radio.setPALevel(RF24_PA_HIGH);
  radio.setChannel(100);
  radio.openWritingPipe(address);
  radio.stopListening();
}

void loop()
{

  while(Serial.available() == 0){} //mengecek data dari program python

  String python_data = Serial.readString(); //membaca data dari program python
    
  if (python_data == "F")
  {
    Send(1); // forward
  }
  
  else if (python_data == "B")
  {
    Send(2); // backward
  }

  else if (python_data == "R")
  {
    Send(3); // turn right
  }

  else if (python_data == "L")
  {
    Send(4); // turn left
  }
  else if (python_data == "S")
  {
    Send(0); // mstop
  }
  
}

void Send(int send_data)//fungsi untuk mengirim sinyal radio ke reciever
{
  radio.write(&send_data, sizeof(send_data));
}
