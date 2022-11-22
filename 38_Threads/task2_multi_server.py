from socket import *
from _thread import *
import threading
import time

print_lock = threading.Lock()

def threaded(connection, sock):
    while True:
        data = connection.recv(1024)
        if not data:
            print('Goodbye')
            print_lock.release()
            break
        if data.decode().lower() == 'stop':
            time.sleep(1)
            sock.close()
            break
        print(f'Server recieved "{data.decode()}"')
        connection.send(data)
    connection.close()


s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 64623))
s.listen(5)

try:
    while True:
        connection, address = s.accept()
        print_lock.acquire()
        print(f'Connected to: {address[0]} : {address[1]}')
        start_new_thread(threaded, (connection, s))
except OSError:
    print('Closed')
