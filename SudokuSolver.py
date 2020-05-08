# Getting the board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def create_board(brd):  # Creating the board
    for i in range(len(brd)):  # For the column

        if i % 3 == 0 and i != 0:  # Print divider after each 3 numbers in the column
            print("- - - - - - - - - - - -")

        for j in range(len(brd[0])):  # For the row

            if j % 3 == 0 and j != 0:  # Print divider after each 3 numbers in the row
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])  # Going back to the next line

            else:
                print(str(brd[i][j]) + " ", end="")


# Finding empty spaces
def find_empty(brd):
    for i in range(len(brd)):  # Selecting the row
        for j in range(len(brd[0])):  # Selecting the column

            if brd[i][j] == 0:  # Check if that position is 0
                return i, j  # positions that have to solve
    return None  # Meaning there is no 0 left


# Check for the valid board
def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:  # check through each number in the row and see if it is equal to the number that just added in. and if it is recently inserted it will be ignored.
            return False
    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:  # check through each number in the column and see if it is equal to the number that just added in. and if it is recently inserted it will be ignored.
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):  # Get to box row wise
        for j in range(box_x * 3, box_x * 3 + 3):  # Get to box column wise
            if brd[i][j] == num and (i, j) != pos:  # check through each box and see if it is equal to the number that just added in. and not checking the same position that just have checked.
                return False
    return True

# Using Backtracking Algorithm
def solve(brd):

    #print(bo)  #For butter understanding

    find = find_empty(brd)
    if not find:  # there is no 0 left
        return True
    else:
        row, col = find
    for i in range(1, 10):  # looping through values 1-10
        if valid(brd, i, (row, col)):  # Checking if it is a valid solution
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0
    return False


create_board(board)
solve(board)
print("The solution")
create_board(board)
