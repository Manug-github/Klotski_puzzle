# https://en.wikipedia.org/wiki/Klotski
import sys 
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
  
sys.setrecursionlimit(10**6) 

def is_solved(board):
    # if board[3][1] == 6:
    #     return True
    if not board:
        return False
    if board[4][1] == 3:
        return True
    return False


def next_movement1(board,used,row,col):

    copy_board = [x[:] for x in board]
    # Mode UP
    if row>0:
        if board[row-1][col]==0:
            board[row-1][col] = 1
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Mode DOWN
    if row<4:
        if board[row+1][col]==0:
            board[row][col] = 0
            board[row+1][col] = 1
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Mode LEFT
    if col>0:
        if board[row][col-1]==0:
            board[row][col-1] = 1
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Mode RIGHT
    if col<3:
        if board[row][col+1]==0:
            board[row][col] = 0
            board[row][col+1] = 1
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    return


def next_movement2(board,used,row,col):
    
    copy_board = [x[:] for x in board]
    print(row,col)
    # Mode UP
    if row>0:
        if board[row-1][col]==0:
            board[row-1][col] = 2
            board[row][col] = 3
            board[row+1][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Mode DOWN
    if row<3:
        if board[row+2][col]==0:
            board[row][col] = 0
            board[row+1][col] = 2
            board[row+2][col] = 3
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    #Move LEFT
    if col>0:
        if board[row][col-1]==0 and board[row+1][col-1]==0:
            board[row][col-1] = 2
            board[row+1][col-1] = 3
            board[row][col] = 0
            board[row+1][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    #Move RIGHT
    if col<3:
        if board[row][col+1]==0 and board[row+1][col+1]==0:
            board[row][col] = 0
            board[row+1][col] = 0
            board[row][col+1] = 2
            board[row+1][col+1] = 3
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    return


def next_movement4(board,used,row,col):

    copy_board = [x[:] for x in board]
    # Move UP
    if row>0:
        if board[row-1][col]==0 and board[row-1][col+1]==0:
            board[row-1][col] = 4
            board[row-1][col+1] = 5
            board[row][col] = 0
            board[row][col+1] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Move DOWN
    if row<4:
        if board[row+1][col]==0 and board[row+1][col+1]==0:
            print("dowww")
            board[row][col] = 0
            board[row][col+1] = 0
            board[row+1][col] = 4
            board[row+1][col+1] = 5
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Mode LEFT
    if col>0 :
        if board[row][col-1]==0:
            board[row][col-1] = 4
            board[row][col] = 5
            board[row][col+1] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    # Mode RIGHT
    if col<2:
        if board[row][col+2]==0:
            board[row][col] = 0
            board[row][col+1] = 4
            board[row][col+2] = 5
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    return


def next_movement6(board,used,row,col):
    copy_board = [x[:] for x in board]
    if row>1:
        if board[row-1][col]==0 and board[row-1][col+1]==0:
            board[row-2][col] = 3
            board[row-1][col] = 2
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    if 0<row<4:
        if board[row+1][col]==0:
            board[row-1][col] = 0
            board[row][col] = 3
            board[row+1][col] = 2
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]


def next_movement(board,used):
    global sol
    print("------------------")
    for row in board:
        print(row)
    print(len(used))
    if is_solved(board):
        print("+++++++++++++")
        sol = [x[:] for x in board]
        return

    if sol:
        return
    for row in range(5):
        for col in range(4):
            if board[row][col] == 1:
                next_movement1(board,used,row,col)
            if board[row][col] == 2:
                next_movement2(board,used,row,col)
            if board[row][col] == 4:
                next_movement4(board,used,row,col)
            # elif board[row][col] == 6:
            #     next_movement6(board,used,row,col)
                

def solve(board,used):
    
    while not is_solved(sol):
        # print(board)
        next_movement(board,used)


board=[
        [2,6,7,2],
        [3,8,9,3],
        [2,4,5,2],
        [3,1,1,3],
        [1,0,0,1]
]

board=[
        [2,2,2,2],
        [3,3,3,3],
        [2,4,5,2],
        [3,1,1,3],
        [1,0,0,1]
]

res = tuple(map(tuple, board)) # Convert list of list in tuple[hashable object].
used = set()
used.add(res)

sol = []
solve(board,used)
print(len(used))
# for use in used:
#     print(use)

print("done")
for row in sol:
    print(row)
