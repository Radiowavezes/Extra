from socket import *


def decryption(recieved_message):
    key = int(recieved_message[0])
    response_message = ''
    caesar_al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for symbol in recieved_message[1:]:
        if symbol.isalpha():
            new_index = (caesar_al.find(symbol) - key) % 52
            symbol = caesar_al[new_index]
        response_message += symbol
    return response_message


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 64623))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f'Connected by {address}')
        while True:
            data = connection.recv(1024)
            response_message = decryption(data.decode('utf-8'))
            if not data:
                break
            connection.sendall(bytes(response_message, encoding='utf-8'))
