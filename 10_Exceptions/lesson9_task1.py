def oops():
    return [1, 2, 'a'][3]


def catcher():
    try:
        oops()
    except IndexError:
        print('Ooops!')


catcher()
