"""
Module to create workers and assighn them to their bosses
"""


class Boss:
    '''
    A class to create a Boss
    ---------
    Atributes:
    id_: int
        to pass uniq id to instanse in order
    self.name: str
        workers name
    self.company: str
        workers company
    self.id_: int
        uniq id, starts with 1000 + 1 (id_)
    self.workers: list
        empty list of workers. Filled with worker instantiating,
    if it belongs to this Boss instant      
    '''

    id_ = 0

    def __init__(self, name: str, company: str):
        Boss.id_ += 1
        self.id_ = 1000 + Boss.id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return f"""
        {self.id_} {self.name} works at {self.company}. He is a boss
        of {len(self.workers)} workers: {self.workers}
        """


class Worker:
    '''
    A class to create a worker
    ----------
    Atributes:
     id_: int
        to pass uniq id to instanse in order
    self.name: str
        workers name
    self.company: str
        workers company
    self.id_: int
        uniq id, starts with 1000 + 1 (id_)
    self._chief: Boss
        the boss of its worker
    '''

    id_ = 0

    def __init__(self, name: str, company: str, chief: Boss):
        Worker.id_ += 1
        self.id_ = 1000 + Worker.id_
        self.name = name
        self.company = company
        self._chief = chief
        chief.workers.append(self.name)

    @property
    def chief(self):
        '''
        Reasings the boss value, if its company attribute is 
        equal to workers company attribute and put the worker
        name attribute to boss instance list of workers
        '''
        return self._chief.name

    @chief.setter
    def chief(self, new_boss):
        try:
            if isinstance(new_boss, Boss):
                if new_boss.company == self.company:
                    self._chief.workers.remove(self.name)
                    self._chief = new_boss
                    new_boss.workers.append(self.name)
                else:
                    raise ValueError
            else:
                raise TypeError
        except (ValueError, TypeError):
            print(f"The boss should have a type <Boss> and work at the {self.company}")

    def __str__(self):
        return f"""
        {self.name} works at {self.company}, her boss is {self._chief.name}
        """


dean = Boss("Dean Winchester", "Supernatural")
alan = Boss("Alan Rickman", "Hogwarts")
bob = Boss("Bob Thornton", "Twitter")
hugo = Boss("Hugo Palma", "Twitter")
mary = Worker("Mary Jane", "Twitter", bob)
print(mary)
print(bob)
mary.chief = hugo
print(mary)
print(hugo)
print(bob)
