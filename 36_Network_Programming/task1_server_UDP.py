from socket import *

HOST = '127.0.0.1'
PORT = 20001
maxsize = 1024
message_from_server = 'Hello UDP client'
bytes_to_send = str.encode(message_from_server)
s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))
print('UDP server up and listening')
while True:
    bytes_addres_pair = s.recvfrom(maxsize)
    message = bytes_addres_pair[0]
    address = bytes_addres_pair[1]
    s.sendto(bytes_to_send, address)
