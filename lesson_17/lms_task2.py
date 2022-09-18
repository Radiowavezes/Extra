class Author:

    ammount = 0

    def __init__(self, name:str, country:str, birthday:int, books = list()):
        self.fname = name
        self.country = country
        self.birthday = birthday
        self.poems = books
        Author.ammount += 1

    def __str__(self):
        return '{} was born on {} in {}'.format(self.fname, self.birthday, self.country)

    def __repr__(self):
        return self.__str__()
class Book:

    summary = 0

    def __init__(self, name:str, year:int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.summary += 1

    def __str__(self):
        return '{} was written in {} by {}'.format(self.name, self.year, self.author)

    def __repr__(self):
        return self.__str__()

class Library:
    def __init__(self, name:str, books = list(), authors = dict()):
        self.title = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        new_book = Book(name, year, author)
        self.books.append((new_book.name, new_book.year, author.fname))
        self.authors[author.fname] = self.authors.get(author.fname, ()) + (new_book.name,)
        author.poems = self.authors.get(author.fname)


    def group_by_author(self, author: Author):
        return self.authors[author.fname]

    def group_by_year(self, year: int):
        for param in self.books:
            if param[1] == year:
                print(param)

    def __str__(self):
        return 'There are {} authors in our {} with {} amount of books'.format(
            Author.ammount,
            self.title,
            Book.summary
            )

    def __repr__(self):
        return self.__str__()


ll = Library('London Library')
william = Author('William Shakespeare', 'Stratford', 1564)
byron = Author('George Byron', 'London', 1824)
joyce = Author('James Joyce', 'Dublin', 1882)
ll.new_book('Prometheus', 1816, byron)
ll.new_book('Cain', 1821, byron)
ll.new_book('Darkness', 1816, byron)
ll.new_book('Manfred', 1817, byron)
ll.new_book('Hamlet', 1603, william)
ll.new_book('Macbeth', 1603, william)
ll.new_book('Othello', 1603, william)
ll.new_book('Romeo and Juliet', 1603, william)
ll.new_book('Dubliners', 1914, joyce)
ll.new_book('Ulysses', 1922, joyce)
ll.new_book('Finnegans Wake', 1939, joyce)
ll.new_book('Exiles', 1918, joyce)
print(ll)
print(byron)
print(Book('Exiles', 1918, joyce))
ll.group_by_year(1603)
print(ll.group_by_author(joyce))
print(ll.group_by_author(william))
print(ll.group_by_author(byron))
print(ll.authors)
print(byron.poems)
print(william.poems)
print(joyce.poems)
print(ll.books)
