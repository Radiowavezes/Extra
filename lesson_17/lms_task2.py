class Author:
    """
    A class to create an author
    Atributes:
    fname: str
        Author name
    city: str
        city of birth
    birthday: int
        year of birth
    books: list
        an empty list to store the books of author
    """

    ammount = 0

    def __init__(self, name: str, city: str, birthday: int, books: list):
        self.fname = name
        self.city = city
        self.birthday = birthday
        self.poems = books
        Author.ammount += 1

    def __str__(self):
        return f"{self.fname} was born on {self.birthday} in {self.city}"

    def __repr__(self):
        return self.__str__()


class Book:
    """
    A class to create a book
    Atributes:
    name: str
        name of the book
    year: int
        the year when it has been written
    author: Author
        the author of it
    """

    summary = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.summary += 1

    def __str__(self):
        return f"{self.name} was written in {self.year} by {self.author}"

    def __repr__(self):
        return self.__str__()


class Library:
    """
    A class to store books and its authors
    Atributes:
    name: str
        Library name
    books: list
        list of data about books (name, year, author)
    authors: dict
        dict of names of authors as keys and their books
        as values
    Methods:
    group_by_author(self, author: Author):
        shows all books of author for his name
    group_by_year(self, year: int):
        shows all books written in sepsific year
    """

    def __init__(self, name: str, books: list, authors: dict):
        self.title = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        """
        i decided to make the dict of authors when adding a new book
        istead of list because in case of list there were every book
        for every author after appending and in author list were 12
        authors instead of 3
        - create new object Book
        - fill the books list with new book, its year and author name
        - fill the dict of authors with author if it's not present in
        dict yet and add the book if it's not in author's tuple of books
        - rewrite the list of author books in object Author with value
        from author dict in object Library
        """
        new_book = Book(name, year, author)
        self.books.append((new_book.name, new_book.year, author.fname))
        self.authors[author.fname] = self.authors.get(author.fname, ()) + (
            new_book.name,
        )
        author.poems = self.authors.get(author.fname)

    def group_by_author(self, author: Author):
        """
        calls the key author.fname in authors dict in Library
        """
        return self.authors[author.fname]

    def group_by_year(self, year: int):
        """
        searches the value equal to year in books list of Library
        on the second position
        """
        for param in self.books:
            if param[1] == year:
                print(param)

    def __str__(self):
        a = Author.ammount
        b = self.title
        c = Book.summary
        return f"There are {a} authors in our {b} with {c} amount of books"

    def __repr__(self):
        return self.__str__()


ll = Library("London Library", [], {})
william = Author("William Shakespeare", "Stratford", 1564, [])
byron = Author("George Byron", "London", 1824, [])
joyce = Author("James Joyce", "Dublin", 1882, [])
ll.new_book("Prometheus", 1816, byron)
ll.new_book("Cain", 1821, byron)
ll.new_book("Darkness", 1816, byron)
ll.new_book("Manfred", 1817, byron)
ll.new_book("Hamlet", 1603, william)
ll.new_book("Macbeth", 1603, william)
ll.new_book("Othello", 1603, william)
ll.new_book("Romeo and Juliet", 1603, william)
ll.new_book("Dubliners", 1914, joyce)
ll.new_book("Ulysses", 1922, joyce)
ll.new_book("Finnegans Wake", 1939, joyce)
ll.new_book("Exiles", 1918, joyce)
print(ll)
print(byron)
print(Book("Exiles", 1918, joyce))
ll.group_by_year(1603)
print(ll.group_by_author(joyce))
print(ll.group_by_author(william))
print(ll.group_by_author(byron))
print(ll.authors)
print(byron.poems)
print(william.poems)
print(joyce.poems)
print(ll.books)
