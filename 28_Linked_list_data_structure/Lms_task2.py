from Lms_task1 import UnorderedList

class NodeStack(UnorderedList):
    
    def push(self, item):
        return super().add(item)
    
    def pop(self):
        return super().pop(0)
    
    def size(self):
        return super().size()
    
    def is_empty(self):
        return super().is_empty()
    
    def get_from_stack(self, item):
        return super().search(item)
    

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
