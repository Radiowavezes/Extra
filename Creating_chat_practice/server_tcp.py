import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 6008)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
message_list = []
users_dict = {}
# a = ''

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = (connection.recv(1024)).decode()
            for value in data.split():
                message_list.append(value)
            user_name = message_list[-2]
            message = message_list[-1]
            users_dict[user_name] = users_dict.get(user_name, message)

            # message_list.append(data)
            print(users_dict)
            print(f'received {message} from {user_name}')
            if data:

                for name, message in users_dict.items():

                    info_ = name + ': ' + message + '\n'
                    
                    connection.sendall(bytes(info_, encoding='utf-8'))

                print('sending data back to the client')
                
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
