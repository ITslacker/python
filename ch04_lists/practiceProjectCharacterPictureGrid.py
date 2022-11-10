"""
Say you have a list of lists where each value in the inner lists is a one-character string, like this:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

Copy the previous grid value, and write code that uses it to print the image.

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].

Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(grid[0][0], grid[1][0], grid[2][0], grid[3][0], grid[4][0], grid[5][0], grid[6][0], grid[7][0], grid[8][0])
print(grid[0][1], grid[1][1], grid[2][1], grid[3][1], grid[4][1], grid[5][1], grid[6][1], grid[7][1], grid[8][1])
print(grid[0][2], grid[1][2], grid[2][2], grid[3][2], grid[4][2], grid[5][2], grid[6][2], grid[7][2], grid[8][2])
print(grid[0][3], grid[1][3], grid[2][3], grid[3][3], grid[4][3], grid[5][3], grid[6][3], grid[7][3], grid[8][3])
print(grid[0][4], grid[1][4], grid[2][4], grid[3][4], grid[4][4], grid[5][3], grid[6][4], grid[7][4], grid[8][4])
print(grid[0][5], grid[1][5], grid[2][5], grid[3][5], grid[4][5], grid[5][5], grid[6][5], grid[7][5], grid[8][5])
print('\n')

print(len(grid))
