from socket import *
import threading


def serving():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 64623))
        s.listen()
        connection, address = s.accept()
        with connection:
            print(f'Connected by {address}')
            while True:
                data = connection.recv(1024)
                if not data:
                    print(threading.current_thread().name, 'Disconnected')
                    break
                connection.sendall(data)

connection1 = threading.Thread(name='Server1', target=serving)

connection1.start()
            