from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 64623))

print("Connected to the server")
message = input('Type your message here: ')
print('sending message:', message)
s.send(message.encode())

answer = s.recv(1024)
print('recv:', answer.decode())
s.close()