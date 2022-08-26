def enclosing_number(number):
    '''including enclosed function
    for multipluing two numbers'''
    def enclosed_number(multiplier):
        return number * multiplier
    return enclosed_number


multiple = enclosing_number(5)
print(multiple(7)) #--> 5 * 7 == 35


def print_message(message):
    '''pylint wants docstring...'''
    def to_print():
        print(message)
    return to_print


another_to_print = print_message('My name is Diksy')
del print_message
another_to_print()
