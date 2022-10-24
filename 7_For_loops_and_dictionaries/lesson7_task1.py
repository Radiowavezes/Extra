with open('input.txt') as inf:
    list_of_words = inf.read().split()
inf.close()
words_dict = {}
for i in list_of_words:
    words_dict[i] = words_dict.get(i, 0) + 1
print(words_dict)
