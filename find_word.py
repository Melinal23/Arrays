"""

A particular grid contains at most one word. The word
may start anywhere in the grid, and consecutive letters can
be either below or to the right of the previous letter.

The input will consist of a word and a grid. Print the
location of the word in the grid as a list of "row column"
coordinates, each on its own line. If the word does not appear
in the grid, just print "None."

Example Input:

catnip

c r c a r s
a b i t n b
t f n n t i
x s i i p t

Example Output:

0 2
0 3
1 3
2 3
3 3
3 4

Clarifications:
- The word will always appear in the grid
exactly 0 or 1 times

"""

def findWord(word, grid):
    coords = []

    found = False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if word[0] == grid[i][j]:
                coords.append((i, j))
                if checkRight(word[1:], grid, i, j + 1, coords) or checkDown(word[1:], grid, i + 1, j, coords):
                    for coord in coords:
                        print(coord[0], coord[1])
                        found = True
                    break
                else:
                    coords = []

    if not found:
        print("None")


def checkRight(word, grid, i, j, coords):
    if word == "":
        return True

    if i >= len(grid) or j >= len(grid[0]):
        return False

    if word[0] == grid[i][j]:
        coords.append((i, j))
        return checkDown(word[1:], grid, i + 1, j, coords) or checkRight(word[1:], grid, i, j + 1, coords)
    else:
        return False


def checkDown(word, grid, i, j, coords):
    if word == "":
        return True

    if i >= len(grid) or j >= len(grid[0]):
        return False

    if word[0] == grid[i][j]:
        coords.append((i, j))
        return checkDown(word[1:], grid, i + 1, j, coords) or checkRight(word[1:], grid, i, j + 1, coords)
    else:
        return False
