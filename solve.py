
def print_board(b):
    
    for r in range(len(b)):
        if r % 3 == 0 and r != 0:
            print("----------------------------")
        
        for c in range(len(b[r])):
            cell = b[r][c]
            
            if c % 3 == 0 and c != 0:
                print("|", end = "")
            
            print(" " + str(cell) + " ", end = "")
        
        print("\n", end = "")

def solve_board(b):
    
    pos = find_empty(b)
    
    if not pos:
        return print_board(b)
    else:
        row, col = pos
        
    for i in range(1, 10):
        if cell_check(b, (row, col), i):
            b[row][col] = i
            
            if solve_board(b):
                return print_board(b)
            
            
            b[row][col] = 0
    
    return False

def find_empty(b):
    
    for r in range(len(b)):
        for c in range(len(b[r])):
            cell = b[r][c]
            
            if cell == 0:
                return((r, c))
    
    return False

def cell_check(b, pos, x):
    
    if row_check(b, pos, x) and col_check(b, pos, x) and sq_check(b, pos, x):
        return True
    else:
        return False
    
def row_check(b, pos, x):
    
    pos_row = pos[0]
    
    if x not in b[pos_row]:
        return True
    else:
        return False

def col_check(b, pos, x):
    
    pos_col = pos[1]
    
    col = [b[r][pos_col] for r in range(len(b))]
    
    if x not in col:
        return True
    else:
        return False

def sq_check(b, pos, x):
    
    pos_row = pos[0]
    pos_col = pos[1]
    
    r_start = pos_row - (pos_row % 3)
    r_end = pos_row + 3 - (pos_row % 3)
    
    c_start = pos_col - (pos_col % 3)
    c_end = pos_col + 3 - (pos_col % 3)
    
    sq = []
    for r in range(r_start, r_end):
        for c in range(c_start, c_end):
            sq.append(b[r][c])
    
    if x not in sq:
        return True
    else:
        return False
    
board1 = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
           [5, 2, 0, 0, 0, 0, 0, 0, 0], 
           [0, 8, 7, 0, 0, 0, 0, 3, 1], 
           [0, 0, 3, 0, 1, 0, 0, 8, 0], 
           [9, 0, 0, 8, 6, 3, 0, 0, 5], 
           [0, 5, 0, 0, 9, 0, 6, 0, 0], 
           [1, 3, 0, 0, 0, 0, 2, 5, 0], 
           [0, 0, 0, 0, 0, 0, 0, 7, 4], 
           [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

solve_board(board1)