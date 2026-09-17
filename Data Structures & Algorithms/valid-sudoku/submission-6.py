#input: 9x9 Sudoku Board (2d array)
#check if 9x9 array is valid

#output: true or false
#questions I would ask: what is the difference between valid and solvable? If the board is empty, would we return true? if the board is full, would we return false? Is it possible for the input to be a larger board? 

#straightforward solution: go through each row, each column, and each 3x3 sub-box, checking for duplicates; Time Complexity = O(n^3), Space Complexity = O(n^2)

#optimal time solution: Store a dictionary of each row, each column, where the key is the sudooku number and the value is the position within the row in separate arrays. One for rows, one for columns. Check for duplicates while storing. Combine respective rows and columns to form dictionaries of sub-boxes. Check those sub-boxes. Time = O(n^2), Space = O(n^2) 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #go through each row and column
        for i in range(9):
            #create a set for that row and column
            row = set()
            column = set()
            for j in range(9):
                #while inserting other elements check if already in set
                #if so, return false
                #skip "." which represent empty spaces
                #otherwise, continue until board is done
                if board[i][j] != ".":
                    if board[i][j] in row:
                        print ("already in row, coords: ", i, j)
                        print (board[i][j])
                        return False
                    row.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in column:
                        print ("already in col, coords: ", j, i)
                        return False
                    column.add(board[j][i])
        for i in range(3):
            for j in range(3):
                sub = set()
                for k in range(3):
                    for l in range(3):
                        if board[k + i*3][l + j*3] != ".":
                            if board[k + i*3][l + j*3] in sub:
                                print (board[k + i*3][l + j*3])
                                print ("already in sub-box, coords: ", k+i*3, l+j*3)
                                return False
                            sub.add(board[k + i*3][l + j*3])
        return True
        #go through each sub-box
        #create sub-box set
        #while inserting sub-box elements
        #check if already in set
        #if so, return false
        #otherwise, continue until sub-box is done
    #return true
    
        