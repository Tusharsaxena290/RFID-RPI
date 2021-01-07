import serial

port = serial.Serial("/dev/serial0",baudrate=9600,timeout=0.5)
people = {"$0005655092":"Rahul","$0013815602":"Sanjay"}
while True:
    rcv = port.readline().decode('utf-8').rstrip()
    print(rcv)
    if(rcv is not ''):
        try:
            print (people[rcv])
        except KeyError:
            print("Authentication Failed")

    
