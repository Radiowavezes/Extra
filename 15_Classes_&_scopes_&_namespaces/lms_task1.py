class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} ", end="")
        print((f"{self.lastname} and I’m {self.age} years old"))


guy = Person("Carl", "Johnson", 26)
Person.talk(guy)
