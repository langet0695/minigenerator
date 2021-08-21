import json
import random


def WordGenerator():
    file = open('/Users/travislange/Desktop/dictionarytest.json', 'r') # contains dict
    commonWords = open('/Users/travislange/Desktop/5000-words.txt', 'r') # 5k most common words
    common = []
    for word in commonWords:
        common.append(word[0:-1])

    f = json.load(file)
    pairs = f.items()
    # destination = open('dict.txt', 'a')
    possible_words = []
    for line in pairs:
        if len(line[0]) == 5 and line[0] in common:
            possible_words.append(line)
        elif len(line[0]) == 4 and line[0] in common:
            newOne = '_' + line[0]
            newTwo = line[0] + '_'
            possible_words.append((newOne, line[1]))
            possible_words.append((newTwo, line[1]))
        elif len(line[0]) == 3 and line[0] in common:
            newOne = '__' + line[0]
            newTwo = line[0] + '__'
            newThree = '_' + line[0] + '_'
            possible_words.append((newOne, line[1]))
            possible_words.append((newTwo, line[1]))
            possible_words.append((newThree, line[1]))
    return possible_words

print(WordGenerator())