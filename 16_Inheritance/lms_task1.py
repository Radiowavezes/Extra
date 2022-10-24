class Person(object):
    def __init__(self, name, y_of_birth, sex, marital):
        self.name = name
        self.b_y = y_of_birth
        self.s = sex
        self.marital = marital

    def __str__(self):
        return f"{self.name} - {self.b_y}, {self.s} - {self.marital}"


class Student(Person):
    def __init__(self, name, y_of_birth, sex, marital, speciality, y_of_grad):
        super().__init__(name, y_of_birth, sex, marital)
        self.spec = speciality
        self.g_y = y_of_grad


class Teacher(Person):
    def __init__(self, name, y_of_birth, sex, marital, salary, diploma, working_exp):
        super().__init__(name, y_of_birth, sex, marital)
        self.salary = salary
        self.diploma = diploma
        self.exp = working_exp

    def __str__(self):
        return f"{self.name} - {self.b_y}, ${self.salary}, {self.diploma} - {self.exp}"


person1 = Person("Annalena Berbok", 1981, "F", "single")
person2 = Student("Boris Johnson", 1989, "M", "married", "Economic", 2011)
degree = ["Bachelor degree of Economic", "Master degree of Law"]
experience = {"2011-2012": "lawyer", "2012 - Present": "Politics"}
person3 = Teacher("Andrzej Duda", 1972, "M", "married", 2000, degree, experience)
print(person1)
print(person2)
print(person3)
