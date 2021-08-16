import json
import random


def WordGenerator():
    file = open('/Users/travislange/Desktop/dictionarytest.json', 'r')
    f = json.load(file)
    pairs = f.items()
    # destination = open('dict.txt', 'a')
    possible_words = []
    for line in pairs:
        if len(line[0]) == 5:
            possible_words.append(line)
        elif len(line[0]) == 4:
            newOne = '_' + line[0]
            newTwo = line[0] + '_'
            possible_words.append((newOne, line[1]))
            possible_words.append((newTwo, line[1]))
        elif len(line[0]) == 3:
            newOne = '__' + line[0]
            newTwo = line[0] + '__'
            newThree = '_' + line[0] + '_'
            possible_words.append((newOne, line[1]))
            possible_words.append((newTwo, line[1]))
            possible_words.append((newThree, line[1]))
    return possible_words

test = WordGenerator()

print(len(test))

random.shuffle(test)
print('done')