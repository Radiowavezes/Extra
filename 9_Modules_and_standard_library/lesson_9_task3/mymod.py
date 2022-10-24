def count_lines(inFile):
    empty_list = [line for line in inFile.readlines()]
    return len(empty_list)

def count_chars(inFile):
    empty_string = ''.join(inFile.read().split())
    reg = 0
    for i in empty_string:
        reg += 1
    return reg

def test(fileName):
    with open(fileName, 'r', encoding='utf8') as inFile:
        a = count_lines(inFile)
    with open(fileName, 'r', encoding='utf8') as inFile:
        b = count_chars(inFile)
    return a, b
