import time


def spinner(seconds):
    for i in range(seconds):
        print('\\\\\\\r\r\r', end='')
        time.sleep(0.5)
        print('|||\r\r\r', end='')
        time.sleep(0.5)
        print('///\r\r\r', end='')
        time.sleep(0.5)
        print('---\r\r\r', end='')
        time.sleep(0.5)


spinner(int(input('How many seconds do you want to watch this??? ')))
