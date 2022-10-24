'''
A simple module with one class with stack implementation
'''

class MyStack:
    '''
    This class implements a stack
    ---
    Attributes:
    self.stack: list[any] - an empty body of the
    future stack
    ---
    Methods:
    push - to add item to the top
    pop - to remove item from the top
    size - current size of the stack
    is_empty - whether stack is empty or not
    get_from_stack - returns a distinct element
    '''

    def __init__(self) -> None:
        self.stack = []

    def push(self, item: any) -> str:
        '''
        Adds item to the top with inserting it to the start
        '''

        self.stack.insert(0, item)
        return f'{item} was added to the stack'

    def pop(self) -> str:
        '''
        Removes item from the top with popping from the start
        '''

        if len(self.stack) > 0:
            item = self.stack.pop(0)
            return f'{item} was being removed from the stack'
        raise ValueError('Stack is empty')

    def size(self) -> str:
        '''
        Returns list length
        '''
        return f'{len(self.stack)}'

    def is_empty(self) -> bool:
        '''
        Cheks if list length is equal to 0
        '''

        return not self.stack

    def get_from_stack(self, item):
        '''
        Returns the item if it is present in stack
        '''

        temp = []
        for unit in self.stack.copy():
            if item == unit:
                temp.extend(self.stack)
                self.stack = temp[:]
                return f'{unit} on {self.stack.index(unit)} index is found'
            temp.append(unit)
            self.stack.pop(0)
        raise ValueError(f'No {item} was found')

    def __str__(self) -> str:
        return f'{list(self.stack)}'


example = MyStack()
print(example.is_empty())
print(example.push(1))
print(example.push(2))
print(example.push(3))
print(example.push(4))
print(example.push(5))
print(example)
print(example.size())
print(example.pop())
print(example.is_empty())
print(example)
print(example.get_from_stack(2))
print(example)
