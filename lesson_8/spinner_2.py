import time


def spinner(seconds, some_list):
    for i in range(seconds):
        for j in range(len(some_list)):
            time.sleep(0.33)
            print(some_list[j], end='')
        

list_of_symb = [
        '\\\\\\\r\r\r', 
        '|||\r\r\r', 
        '///\r\r\r', 
        '---\r\r\r']


spinner(int(input('How long do you want to watch this??? Seconds --> ')), list_of_symb)
