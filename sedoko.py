def validSudoko(board):
    rowSet=[set() for _ in range(9)]
    colSet=[set() for _ in range(9)]
    gridSet=[set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if(board[i][j]=="."):
                continue
            GridNo=(i//3)*3+(j//3)
            isPresentinRow = board[i][j] in rowSet[i]
            isPresentinCol = board[i][j] in colSet[j]
            isPresentinGrid = board[i][j] in gridSet[GridNo]

            if(isPresentinRow or isPresentinCol or isPresentinGrid):
                                       return False
            rowSet[i].add(board[i][j])
            colSet[j].add(board[i][j])
            gridSet[GridNo].add(board[i][j])
    return True
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(validSudoko(board))

                
