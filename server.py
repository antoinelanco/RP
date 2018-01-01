import socket, sys
import time
import threading




def receve(client, address):

    print "{} connected".format( address )

    response = client.recv(255)
    if response != "":
            print response

    pass
pass


host = "192.168.1.43" # IP server
port = 60000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(host+" "+`port`)
socket.bind((host, port))

socket.listen(5)
while True:
    client, address = socket.accept()
    receve(client,address)
pass
print "Close"
client.close()
stock.close()
