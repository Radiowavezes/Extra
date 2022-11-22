import threading

class Counter(threading.Thread):
    
    counter = 0
    rounds = 100000
    
    def run(self):
        print(threading.current_thread().name, 'Starting...') # to figure out if join works
        for _ in range(Counter.rounds):
            Counter.counter += 1
        print(threading.current_thread().name, '...ending') # to figure out if join works

def task():
    counter1 = Counter
    counter2 = Counter
        
    thread1 = threading.Thread(target=Counter.run(counter1))
    thread2 = threading.Thread(target=Counter.run(counter2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

for i in range(10):
    task()
    print(Counter.counter)
