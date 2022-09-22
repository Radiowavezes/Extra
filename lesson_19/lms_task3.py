class MyIterator:
    def __init__(self, stop:int):
        self.stop = stop
        self.start = 0
        self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        self.start += 1
        return self.start - 1

class MyGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current <= self.stop:
            yield current
            current += 1


a = MyIterator(10)
b = [i for i in a]
c = iter(a)
print(b)
print(c)
from_to = MyGenerator(1, 10)
print(*from_to)
