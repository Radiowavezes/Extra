import multiprocessing
from socket import *

def handle(conn, addr):
    print("Starting")
    
    message = conn.recv(1024)
    print("Client:", addr, 'recv:', message.decode())
    
    answer = "Bye!"
    conn.send(answer.encode())
    print("Client:", addr, 'send:', answer)
    
    print("Ending")
    conn.close()

   
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('127.0.0.1', 64623))
    s.listen(5)

    try:
        while True:
            print("Waiting for client")
            conn, addr = s.accept()
        
            print("Client:", addr)
            
            process = multiprocessing.Process(target=handle, args=(conn, addr))
            process.start()
        
    except KeyboardInterrupt:
        print("Cancelled")
        
    finally:
        for process in multiprocessing.active_children():
            print("Shutting down process %r", process)
            process.terminate()
            process.join()
            print("All done")

if __name__=="__main__":
    main()