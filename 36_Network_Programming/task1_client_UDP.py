from socket import *

HOST = '127.0.0.1'
PORT = 20001
maxsize = 1024
message_from_client = 'Hello UDP server'
bytes_to_send = str.encode(message_from_client)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(bytes_to_send, (HOST, PORT))
message_from_server, address = s.recvfrom(256)
print(message_from_server)
