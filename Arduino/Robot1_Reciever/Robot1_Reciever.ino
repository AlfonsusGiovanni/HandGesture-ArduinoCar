#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <NewPing.h>

#define CE_PIN   9
#define CSN_PIN 10
#define LED 4
//  #define echo_pin A1
//  #define trigger_pin A0
//  #define max_distance 200

//  NewPing sonar(echo_pin, trigger_pin, max_distance);

// Inialisasi pin pada L298N
int enA = 6; // enable motor A // pin 6 = pwm pin
int enB = 5; // enable motor B // pin 5 = pwm pin
const int in1 = 8; // motor A1 pin (+)
const int in2 = 7; // motor A2 pin (-)
const int in3 = 4; // motor B1 pin (-)
const int in4 = 3; // motor B2 pin (+)

RF24 radio(CE_PIN, CSN_PIN); // Inialisasi pin CE dan CSN pada nRF24L01
const byte address[6] = "00001"; // Alamat komunikasi

//int jarak;

/////////////////////////////////////////////////////////////

void setup() 
{
  Serial.begin(9600);
  
  //setup reciever nrf240L1
  radio.begin();
  radio.setAutoAck(false);
  radio.setDataRate(RF24_250KBPS);
  radio.setPALevel(RF24_PA_MIN);
  radio.setChannel(100);
  radio.openReadingPipe(0, address);
  radio.startListening();

  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(LED, OUTPUT);
}

void loop()
{

  if (radio.available()) //mengecek sinyal transmiter
  {
      //pinMode(LED, HIGH);
      int command;
      radio.read(&command, sizeof(command));
     
      switch (command)
      {
        case 0:
          //digitalWrite(LED, LOW);
          mstop();
          delay(100);
          break;

        case 1:
          //digitalWrite(LED, HIGH);
          forward();
          delay(100);
          break;

        case 2:
          //digitalWrite(LED, HIGH);
          backward();
          delay(100);
          break;

        case 3:
          //digitalWrite(LED, HIGH);
          turn_right();
          delay(100);
          break;

        case 4:
          //digitalWrite(LED, HIGH);
          turn_left();
          delay(100);
          break;
      }     
  }
}

void ns() //normal speed set
{
  analogWrite(enA, 150);
  analogWrite(enB, 150);
}

void zp() //zero speed set
{
  analogWrite(enA, 0);
  analogWrite(enB, 0);
}

void forward() //pin positif motor A dan B menyala
{
  Serial.println("maju");
  digitalWrite(in1, HIGH); 
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);

  ns();
}

void backward() //pin positif motor A dan B mati
{
  Serial.println("mundur");
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  
  ns();
}

void turn_left() //pin positif motor B menyala dan motor A mati
{
  Serial.println("kiri");
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  
  analogWrite(enA, 200);
  
}

void turn_right() //pin positif motor A menyala dan motor B mati
{
  Serial.println("kanan");
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  
  analogWrite(enB, 200);
  
}

void mstop() //semua pin motor A dan B mati
{
  Serial.println("stop");
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  zp();
}
