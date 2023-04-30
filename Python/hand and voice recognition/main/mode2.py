import serial
import SpeechControlModule as scm
import time

# Arduino Setup
arduino = serial.Serial('COM6', 9600)
arduino.timeout = 1

def stop():
    motor_write = "S"
    arduino.write(motor_write.encode())
    print("STOP")

while True:

        query = scm.take_command().lower()

        if 'move forward' in query:
            motor_write = "F"
            arduino.write(motor_write.encode())
            time.sleep(2)
            stop()

        elif 'move backward' in query:
            motor_write = "B"
            arduino.write(motor_write.encode())
            time.sleep(2)
            stop()

        elif 'turn left' in query:
            motor_write = "L"
            arduino.write(motor_write.encode())
            time.sleep(5)
            stop()

        elif 'turn right' in query:
            motor_write = "R"
            arduino.write(motor_write.encode())
            time.sleep(5)
            stop()

        elif 'stop' in query:
            stop()

        elif 'off please' in query:
            print("See you next time sir")
            break

        else:
            print("Voice not recognized")