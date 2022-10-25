from Lms_task1 import Node

class NodeStack:
    def __init__(self):
        self._head = None
    
    def push(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
    
    def pop(self):
        current = self._head
        self._head = current.get_next()
    
    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
            
    def is_empty(self):
        return self._head is None
    
    def get_from_stack(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found
    
    def __repr__(self):
        representation = ""
        current = self._head
        while current is not None:
            representation += f"<- {current.get_data()} "
            current = current.get_next()
        return representation
    

example = NodeStack()
example.push(22)
print(example)
example.push(33)
print(example)
example.push(44)
print(example)
example.push(55)
print(example)
example.pop()
print(example)
example.pop()
print(example)
example.pop()
print(example)
example.pop()
print(example)
