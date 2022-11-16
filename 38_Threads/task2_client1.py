from socket import *

message = 'Hello from client1'

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 64623))
    s.sendall(bytes(message, encoding='utf-8'))
    data = s.recv(1024)
    
print(f'Received {data!r}')
