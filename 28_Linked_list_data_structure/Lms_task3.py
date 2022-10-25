from Lms_task1 import Node

class NodeQueue:
    def __init__(self):
        self._head = None

    def enqueue(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
    
    def dequeue(self):
        current = self._head
        next = self._head.get_next()
        if next:
            while next and current:
                if next.get_next():
                    current = next
                    next = next.get_next()
                else:
                    current.set_next(None)
                    break
        else:
            self._head = None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
    
    def is_empty(self):
        return self._head is None
    
    def get_from_queue(self, item):
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
            representation += f"<-> {current.get_data()} "
            current = current.get_next()
        return representation

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
    