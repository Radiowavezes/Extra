import time


def spinner(seconds, some_list, now_time, n=3):
    while True:
        current_time = time.time()
        elapsed_time = current_time - now_time
        if elapsed_time > seconds:
            break
        else:
            for symbol in some_list:
                print(symbol * n, end='')
                time.sleep(0.33)
                print('\r' * n, end='')

        

list_of_symb = ['\\', '|', '/', '-']


spinner(int(input('How long do you want to watch this??? Seconds --> ')), list_of_symb, time.time())
