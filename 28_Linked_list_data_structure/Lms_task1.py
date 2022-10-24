class Node:
    '''
    Class creates a Node for node structures
    ----------
    Attributes:
    - self._data - current element
    - self._next - connection to the next element for the current
    --------
    Methods:
    - get_data - shows the value of current Node
    - get_next - shows the next value for the Node
    - set_data - sets the value as current for Node
    - set_next - sets the value as next for Node
    
    '''
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
    '''
    Class creates a node list
    ----------
    Atributes:
    - self._head - list's body
    --------
    Methods:
    - is_empty - shows if the list is empty
    - add - to add node to the begining of the nodelist
    - append - to add node to the end of the nodelist
    - index - returns a node on the specified position
    - slice_index - returns an index of a specified node
        !!! also slice_index is used for __getitem__ magic
        method to get a full indexed dictionary values !!!
    -  pop - pops and returns the element with the given
    index. With no index pops the last element. Negative
    indexes are also allowed
    - size - returns the length of the nodelist
    - search - boolean functions, shows if the value is 
    present in the nodelist or not
    - remove - removes a specified value from the nodelist
    '''

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
    
    def index(self, number):
        indexed_list = {}
        current = self._head
        while current:
            for index in range(self.size()):
                indexed_list[current.get_data()] = index
                current = current.get_next()
        return indexed_list[number]
    
    def slice_index(self, number=None):
        indexed_list = {}
        current = self._head
        while current:
            for index in range(self.size()):
                indexed_list[index] = current.get_data()
                current = current.get_next()
        if number is None:
            return indexed_list.values()
        else:
            return indexed_list[number]
    
    def pop(self, number=None):
        if number is None:
            number = self.size() - 1
        elif number < 0:
            number += self.size()
        to_pop = self.slice_index(number)
        self.remove(to_pop)
        return to_pop
    
    def __getitem__(self, number):
        if isinstance(number, slice):
            return list(list(self.slice_index()).__getitem__(number))
        else:
            return self.slice_index(number)

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
        representation = ""
        current = self._head
        while current is not None:
            representation += f"<- {current.get_data()} "
            current = current.get_next()
        return representation



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
    print(my_list.pop(0))
    print(my_list)
    print(my_list[2:5])
    print(my_list[3])
