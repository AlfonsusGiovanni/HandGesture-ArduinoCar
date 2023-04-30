import keyboard
import serial
import time

# Arduino Setup
arduino = serial.Serial('COM5', 9600)
arduino.timeout = 1

def stop():
    motor_write = "S"
    arduino.write(motor_write.encode())
    print("STOP")
    time.sleep(0.1)

def forward():
    motor_write = "F"
    arduino.write(motor_write.encode())
    print("MOVE FORWARD")
    time.sleep(0.1)

def backward():
    motor_write = "B"
    arduino.write(motor_write.encode())
    print("MOVE BACKWARD")
    time.sleep(0.1)

def turn_left():
    motor_write = "L"
    arduino.write(motor_write.encode())
    print("TURN LEFT")
    time.sleep(0.1)

def turn_right():
    motor_write = "R"
    arduino.write(motor_write.encode())
    print("TURN RIGHT")
    time.sleep(0.1)


while True:

    IsPressed = False

    while not IsPressed:
        if keyboard.is_pressed('w'):
            forward()
            IsPressed = True

        elif keyboard.is_pressed('a'):
            turn_left()
            IsPressed = True

        elif keyboard.is_pressed('s'):
            backward()
            IsPressed = True

        elif keyboard.is_pressed('d'):
            turn_right()
            IsPressed = True

        elif IsPressed == False:
            stop()