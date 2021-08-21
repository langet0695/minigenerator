# Author: Travis Lange
# Description: This is an experiment to develop an algorithm that can generate a mini cross word (5x5) puzzle.

# TO DO:
# v1 DONE Create a list of tuples containing (word, hint)
# Create a board that is a 5 element array with 5 nested arrays of length 5
# Population stage
# While loop to iterate over list of tuples checking to see what can be added
# If statements to check if a word can be added horizontally
# If statements to check if word can be added vertically
# break once a mini meets succes criteria (e.g. 5 horizontal words and ok vertical statements)
# break if unsuccessful
# Print out populated board + hints by row and column

# Add step back functionality to remove a row if the word doesn't work
# Add memory to not count a word if checked once
import random
import json
import dictConfig
possible_words = dictConfig.WordGenerator()
#
#
#
# possible_words = [
#     ("pass_", "test"),
#     ("open_", "test"),
#     ("tapas", "_"),
#     ("_rice", "_"),
#     ("_take", "test"),
#     ("pot__", "test"),
#     ("apart", "test"),
#     ("sepia", "test"),
#     ("snack", "test"),
#     ("__see", "test"),
#     ("SODAS", "Fast-food drinks"),
#     ("TOROS", "Corrida de ___ (“Running of the Bulls”)"),
#     ("SHAME", "Feeling of humiliation"),
#     ("OCEAN", "Separator of continents"),
#     ("_CABS", "Yellow symbols of N.Y.C."),
#     ("_NESS", "Loch ___ monster"),
#     ("SAMOA", "Girl Scout cookie sprinkled with coconut"),
#     ("BEARD", "Dopey is the only one of the Seven Dwarfs without one"),
#     ("ACHOO", "Sound preceding Bless you!"),
#     ("COSTS", "Counterpart of benefits, in a business analysis"),
#     ("_bag_", "something placed in an overhead compartment"),
#     ("sarah", "comedian Silverman"),
#     ("argue", "make the case for"),
#     ("doozy", "total wower"),
#     ("_nne_", "opposite of SSW"),
#     ("baron", "industry tycoon"),
#     ("argon", "element suggested here NOPQSTU"),
#     ("gauze", "wrap in a first aid kit"),
#     ("_sad_", "feeling blue"),
#     ("_hey_", "what the...")
# ]

failures = []

board = [
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"]
]


def boardConstructor(possibilties, boardName, failures=[]):
    row = 0
    loop_count = 0
    topLineFail = []
    while row < 5:
        for word in possibilties:
            # print("exploring a new word: ", word[0])
            if row < 5:
                if word[0] not in failures:
                    if addWord(boardName, word[0], row) is True:
                        # print("This is the row we added: ", row)
                        # printBoard(boardName)
                        row = row + 1
                        loop_count = 0
                        # failures = []

        loop_count += 1
        if loop_count > 1 and row != 0:
            row -= 1
            removeWord(boardName, row, failures)
            loop_count = 0
            print('did not make it')
            print('this is the row ', row)
            # if row >= 3:
            #     printBoard(boardName)
            #     break
            # print('breakout')
            # print('this is row', row)
            # break
        elif loop_count > 1 and row == 0:
            failures = []
            print('failure')
            random.shuffle(possibilties)
    # printBoard(boardName)
    # print('failures', failures)
    return boardName

def removeWord(aboard, row=0, failures=[]):
    """ Method to remove a word"""
    removalWord = ''

    #if aboard[row] == ["_", "_", "_", "_", "_"]:
    #print("Throught if filter")
    for position in range(0, 5):  # add word to new empty row
        removalWord = removalWord + aboard[row][position]
        # print(removalWord)

    failures.append(removalWord)
    aboard[row] = ["_", "_", "_", "_", "_"]
    # print(failures)


def addWord(aboard, word, row=0):
    """ Method to check and see if a word can be added"""
    # print("entering add word: ", word)
    # print("this is row:", row)
    # print("this is board[row]: ", aboard[row])

    #if aboard[row] == ["_", "_", "_", "_", "_"]:
    #print("Throught if filter")
    for position in range(0, 5):  # add word to new empty row
        letter = word[position]
        aboard[row][position] = letter

    vWord0 = ""
    vWord1 = ""
    vWord2 = ""
    vWord3 = ""
    vWord4 = ""

    word_true = [0, 0, 0, 0, 0]  # creates an array with 0 bools in each position.
                                # We will know our word doesn't fit if there are any 0's at the end.

    for row in range(0, row + 1):  # construct the beginning of each column word
        for column in range(0, 5):
            if column == 0:
                vWord0 = vWord0 + aboard[row][column]
                # print('this is vWord0: ', vWord0)
            if column == 1:
                vWord1 = vWord1 + aboard[row][column]
                # print('this is vWord1: ', vWord1)
            if column == 2:
                # print("This is vWord2: ", vWord2)
                vWord2 = vWord2 + aboard[row][column]
                # print("This is vWord2: ", vWord2)
            if column == 3:
                # print("This is vWord3: ", vWord3)
                vWord3 = vWord3 + aboard[row][column]
                # print("This is vWord3: ", vWord3)
            if column == 4:
                # print("This is vWord4: ", vWord4)
                vWord4 = vWord4 + aboard[row][column]
                # print("This is vWord4: ", vWord4)

    for element in possible_words:
        # print("Ths is element word: ", element[0])
        if vWord0 in element[0]:
            # print("word0 is in")
            word_true[0] = 1
        if vWord1 in element[0]:
            # print("vword1 is in: ", vWord1)
            word_true[1] = 1
        if vWord2 in element[0]:
            # print("vword2 is in: ", vWord2)
            word_true[2] = 1
        if vWord3 in element[0]:
            word_true[3] = 1
        if vWord4 in element[0]:
            word_true[4] = 1
    # print("this is word_true: ", word_true)
    if 0 in word_true:
        # print('no go')
        for position in range(0, 5):  # add word to new empty row
            aboard[row][position] = "_"
        return False
    else:
        # print("we have a true")
        row += 1
        return True


def printBoard(board):
    for row in board:
        print(row)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('this is the start')
    printBoard(board)

    random.shuffle(possible_words)
    boardConstructor(possible_words, board, failures)

    print('this is the end')
    printBoard(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
