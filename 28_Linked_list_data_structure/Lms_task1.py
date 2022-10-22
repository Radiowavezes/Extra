class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):
        current = self._head
        previous = None
        while current:
            if current.get_next():
                previous = current
                current = current.get_next()
            else:
                temp = Node(item)
                previous.set_next(current)
                current.set_next(temp)
                break
    
    def index(self, number=None):
        indexed_list = {}
        current = self._head
        while current:
            for index in range(self.size()):
                indexed_list[current.get_data()] = index
                current = current.get_next()
        if number is not None:
            return indexed_list[number]
        return indexed_list
    
    def slice(self, number):
        indexed_list = {}
        current = self._head
        while current:
            for index in range(self.size()):
                indexed_list[index] = current.get_data()
                current = current.get_next()
        return indexed_list[number]
    
    def pop(self, number):
        to_pop = self.slice(number)
        self.remove(self.slice(number))
        return to_pop
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return list(list(self.index()).__getitem__(key))
        else:
            return self.slice(key)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"<- {current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.append(22)

    # print(my_list.size())
    print(my_list)
    # print(my_list.search(93))
    # print(my_list.search(100))

    # my_list.add(100)
    # print(my_list.search(100))
    # print(my_list.size())

    # my_list.remove(54)
    # print(my_list.size())
    # my_list.remove(93)
    # print(my_list.size())
    # my_list.remove(31)
    # print(my_list.size())
    # print(my_list.search(93))
    print(my_list.index(26))
    print(my_list)
    print(my_list.pop(3))
    print(my_list)
    print(my_list[2:5])
    print(my_list[3])
