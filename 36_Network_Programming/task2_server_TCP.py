from socket import *


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 64623))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f'Connected by {address}')
        while True:
            data = connection.recv(1024)
            recieved_message = data.decode('utf-8')
            response_message = ''
            caesar_al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for symbol in recieved_message:
                if symbol.isalpha():
                    new_index = (caesar_al.find(symbol) + 3) % 52
                    symbol = caesar_al[new_index]
                response_message += symbol
                 
            if not data:
                break
            connection.sendall(bytes(response_message, encoding='utf-8'))
