#inspired from tech with tim

#code to solve
def solver(board):
    empty=find(board)
    if not empty:
        return True
    else:
        row,col=empty
    for i in range(1,10):
        if correct(board,i,empty):
            board[row][col]=i

            if solver(board):
                return True
            board[row][col]=0
    return False

#validates value with position
def correct(board,key,position):
    for i in range(len(board)):
        if board[position[0]][i]==key and position[1]!=i:
            return False
    
    for i in range(len(board[0])):
        if board[i][position[1]]==key and position[0]!=i:
            return False
    
    row_box=position[0]//3
    col_box=position[1]//3

    for i in range(row_box*3,row_box*3+3):
        for j in range(col_box*3,col_box*3+3):
            if board[i][j]==key and position[0]!=i and position[1]!=j:
                return False
    return True

#code to find empty slot
def find(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")
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
solver(board)
print_board(board)
