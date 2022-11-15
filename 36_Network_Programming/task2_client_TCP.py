from socket import *

passkey = 3
message = input('Please, input your message here: ')

def encryption(recieved_message, key):
    response_message = ''
    caesar_al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for symbol in recieved_message:
        if symbol.isalpha():
            new_index = (caesar_al.find(symbol) + key) % 52
            symbol = caesar_al[new_index]
        response_message += symbol
    return response_message

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 64623))
    s.sendall(bytes(encryption(message, passkey), encoding='utf-8'))
    data = s.recv(1024)

print(f'Received {data!r}')
 