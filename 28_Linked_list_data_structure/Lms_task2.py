from Lms_task1 import UnorderedList

class NodeStack(UnorderedList):
    
    def push(self, item):
        return super().append(item)
    
    def pop(self, number=None):
        return super().pop(number)
    
    def size(self):
        return super().size()
    
    def is_empty(self):
        return super().is_empty()
    
    def get_from_stack(self, item):
        return super().search(item)
    
    def __repr__(self):
        return super().__repr__()

example = NodeStack()
example.push(22)
example.push(33)
example.push(44)
print(example)
