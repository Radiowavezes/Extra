'''
Queue with cheking if a sequence of special characters is correct
'''

class MyQueue:
    '''
    Queue accepts the symbols of phrase and cheks if braces are being added correctly
    to its pair. The operation of removing the element, started with any opening brace,
    impacts on every next symbol and removes each unless it meets a closing brace.
    ---------
    Atributes:
    self.queue: list[any] - a body of queue
    self.pairs: dict - pairs of brackets to check if a sequence is valid in enqueue and 
    dequeue methods
    ---------
    Methods:
    enqueue - to add element
    dequeue - to remove element
    size - shows the current size of the queue
    is_empty - shows wether the queue is empty
    get_from_queue - returns a distinct element
    '''

    def __init__(self, queue: list) -> None:
        self.queue = queue
        self.pairs = {')':'(', '}':'{', ']':'[', '(':')', '{':'}', '[':']'}

    def enqueue(self, item) -> None:
        '''
        If you try to add a closing brace, method will check, if its opening brace is
        present. Otherwise it causes an error
        '''
        if item in '([{)}]':
            for unit in self.queue[::-1]:
                if unit == item:
                    raise ValueError('Incorrect braces')
                elif unit == self.pairs[item]:
                    self.queue.append(item)
                    break
        else:
            self.queue.append(item)


    def dequeue(self) -> None:
        '''
        In case removing the elements starts from the begining, this method
        cheks if you try to remove an opening brace and if you do, it will
        remove it with closing brace and every symbol between them
        '''
        if len(self.queue) < 1:
            raise ValueError('Empty queue')
        else:
            if str(self.queue[0]) in '([{':
                item = self.queue[0]
                self.queue.pop(0)
                for unit in self.queue:
                    if unit == self.pairs[item]:
                        self.queue.pop(0)
                        break
                    self.queue.pop(0)
            else:
                self.queue.pop(0)

    def size(self) -> int:
        '''
        Shows the queue length
        '''
        return len(self.queue)

    def is_empty(self) -> bool:
        '''
        Cheks if the length of the queue is equal to 0
        '''
        return not self.queue

    def get_from_queue(self, item):
        '''
        Returns the item if it is present in queue
        '''
        
        temp = []
        for unit in self.queue.copy():
            if item == unit:
                temp.extend(self.queue)
                self.queue = temp[:]
                return f'{unit} on {self.queue.index(unit)} index is found'
            temp.append(unit)
            self.queue.pop(0)
        raise ValueError(f'No {item} was found')

    def __str__(self):
        return f'{list(self.queue)}'


example = MyQueue([1, 2, 'my', 3, '(', 'name', ')', 4, 5,])
print(example.enqueue('('))
print(example.enqueue(')'))
print(example)
example.dequeue()
example.dequeue()
example.dequeue()
print(example)
print(example.get_from_queue('name'))
print(example)
