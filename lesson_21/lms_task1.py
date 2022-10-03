from datetime import datetime

class OpenFile:

    counter = 0

    def __init__(self, name, method='a+'):
        self.file = open(name, method, encoding='utf8')
        self.logs = open('logs.txt', 'a+', encoding='utf8')

    def __enter__(self):
        OpenFile.counter += 1
        return self.file

    def __exit__(self, *exc):
        if any(exc):
            print('It works with errors')
            self.logs.write(f'{str(exc)}\n')
        self.logs.write(f'{OpenFile.counter}\n')
        self.logs.write(f'{datetime.now()}\n')
        self.file.close()


# with OpenFile('Hello') as inF:
#     inF.write('Hello!\n')

# with OpenFile('Hello') as inF:
#     inF.write('Python!\n')

# with OpenFile('Hello') as inF:
#     inF.write('Today!\n')

# with OpenFile('Hello') as inF:
#     inF.write('is Friday!\n')
