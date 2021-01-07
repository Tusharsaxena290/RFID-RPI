import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('Enter Name: ')
        print("Place RF Tag/Card")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
