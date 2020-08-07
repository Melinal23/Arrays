# Given a list of words and an M x N board of characters, find all possible words in the list
# that can be formed by a sequence of adjacent characters on the board.
#
# Input: words = ["GUEST", "FOR", "ARE", "QUIT"]
#        board = [['G', 'I', 'Z'],
#                 ['A', 'U', 'T'],
#                 ['Q', 'S', 'E']];
#
# Output:  "GUEST", "QUIT"


def find_words(array):

    if len(array) == 0:
        return None

    curr = None

    for element in array:
        for char in element:
            curr = char

    



array1 = ["GUEST", "QUIT"]

print(find_words(array1))

