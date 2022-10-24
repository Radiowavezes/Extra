from Lms_task1 import UnorderedList

class NodeQueue(UnorderedList):

    def enqueue(self, item):
        return super().add(item)
    
    def dequeue(self):
        return super().pop()
    
    def size(self):
        return super().size()
    
    def is_empty(self):
        return super().is_empty()
    
    def get_from_queue(self, item):
        return super().search(item)

example = NodeQueue()
example.enqueue(22)
print(example)
example.enqueue(33)
print(example)
example.enqueue(44)
print(example)
example.enqueue(55)
print(example)
example.dequeue()
print(example)
example.dequeue()
print(example)
example.dequeue()
print(example)
example.dequeue()
print(example)

    