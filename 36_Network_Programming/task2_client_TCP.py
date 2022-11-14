from socket import *
key = (input('Input the key for message to decrypt 1-9: '))
message = 'WrgdB lv d jrrg gdB!'

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 64623))
    s.sendall(bytes(key, encoding='utf-8'))
    s.sendall(bytes(message, encoding='utf-8'))
    data = s.recv(1024)

print(f'Received {data!r}')
