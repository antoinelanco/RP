import socket
import time
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
host = "192.168.1.30" # IP server
port = 60000

GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)
stat = 0

while True :
    time.sleep(0.1)
    stat21 = GPIO.input(21)
    stat20 = GPIO.input(20)

    if stat20 == 1:
        stat = 20
        break
        pass
    if stat21 == 1:
        stat = 21
        break
        pass
pass

print("connected")
print(host)
print(port)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
print "Connection on {}".format(port)

socket.send(u"Ton rpi n1 et declancher sur la pin "+`stat`)

socket.close()
