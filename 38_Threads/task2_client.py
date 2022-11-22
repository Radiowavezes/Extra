from socket import *


s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 64623))

while True:
    message = input('Type your message here: ')
    s.send(message.encode())
    if message.lower() == 'stop':
        break
    data = s.recv(1024)
    print(f'Data from server: "{data.decode()}"')
    answer = input('\nDo you want to continue(y/n): ')
    if answer == 'y':
        continue
    else:
        break
s.close()
