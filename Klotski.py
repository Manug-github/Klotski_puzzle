# https://en.wikipedia.org/wiki/Klotski


def is_solved(board):
    # if board[3][1] == 6:
    #     return True
    if not board:
        return False
    if board[0][0] == 1:
        return True
    return False


def next_movement1(board,used,row,col):

    copy_board = [x[:] for x in board]
    if row>0:
        if board[row-1][col]==0:
            board[row-1][col] = 1
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    if row<4:
        if board[row+1][col]==0:
            board[row+1][col] = 1
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]

    if col>0:
        if board[row][col-1]==0:
            board[row][col-1] = 1
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    if col<3:
        if board[row][col+1]==0:
            board[row][col+1] = 1
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    return


def next_movement2(board,used,row,col):
    copy_board = [x[:] for x in board]
    if row>1:
        if board[row-2][col]==0:
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

    if col>0 and row>0:
        if board[row-1][col-1]==0 and board[row][col-1]==0:
            board[row-1][col-1] = 3
            board[row][col-1] = 2
            board[row-1][col] = 0
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    if col<3 and row>0:
        if board[row-1][col+1]==0 and board[row][col+1]==0:
            board[row-1][col+1] = 3
            board[row][col+1] = 2
            board[row-1][col] = 0
            board[row][col] = 0
            res = tuple(map(tuple, board))
            if res not in used:
                used.add(res)
                next_movement(board,used)
            board = [x[:] for x in copy_board]
    return

def next_movement4(board,used,row,col):
    pass

def next_movement6(board,used,row,col):
    pass

def next_movement(board,used):
    global sol
    print("------------------")
    for row in board:
        print(row)

    if is_solved(board):
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
            # elif board[row][col] == 4:
            #     next_movement4(board,used,row,col)
            # elif board[row][col] == 6:
            #     next_movement6(board,used,row,col)
                

def solve(board,used):
    
    while not is_solved(sol):
        print(board)
        next_movement(board,used)


board=[
        [3,6,7,3],
        [2,8,9,2],
        [3,4,5,3],
        [2,1,1,2],
        [1,0,0,1]
]

board=[
        [3,6,7,3],
        [2,8,9,2],
        [3,1,1,3],
        [2,0,0,2],
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
