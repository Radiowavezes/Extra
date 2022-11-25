import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6008      # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    name_user = input("Your name: ")
    message = input("Your message: ")
    user_info = name_user + ' ' + message
    s.sendall(user_info.encode())
    # s.sendall(message.encode())
    data = s.recv(1024)

print(data.decode())
