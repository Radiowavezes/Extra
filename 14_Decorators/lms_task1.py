import random

def logger(f):
    def decorating(*args, **kwargs):
        print(f.__name__, f'with {f.__code__.co_nlocals} args', *args, **kwargs)
        return f(*args, **kwargs)
    return decorating

@logger
def some_function(my_list):
    return [i**3 for i in my_list]

cubes = [random.randrange(20) for number in range(10)]
print(some_function(cubes))
