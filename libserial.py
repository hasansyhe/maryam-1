import serial

port = serial.Serial("/dev/ttyACM0")
print (port.name)
port.write(b"AT\r")

u = input("enter")
if u == "y":
    port.close()
