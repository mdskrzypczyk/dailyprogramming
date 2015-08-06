from sys import argv

move_space = "abcdefg"
gameboard = [['.' for x in range(7)] for x in range(6)]

def place_move(column, player):
    col = move_space.index(column.lower())
    for row in range(6):
        if gameboard[row][col] == '.':
            gameboard[row][col] = player
            return [row,col]

    return None

def check_win(last_move,p):
    lrow,lcol = last_move
    return check_row(lrow,p) or check_col(lcol,p) or check_diagonal(lrow,lcol,p)

def check_row(row,p):
    return  p*4 in ''.join(gameboard[row])

def check_col(col,p):
    column = [gameboard[x][col] for x in range(6)]
    return  p*4 in ''.join(column)

def check_diagonal(row,col,p):
    start1 = [row-min(row,col),col-min(row,col)]
    spaces1 = min(5-start1[0],6-start1[1])
    start2 = [row+min(5-row,col),col-min(5-row,col)]
    spaces2 = min(start2[0]+1, 6-start2[1])
    print row,col,start1,spaces1,start2,spaces2
    return p*4 in "".join([gameboard[start1[0]+i][start1[1]+i] for i in range(spaces1)]) or p*4 in"".join([gameboard[start2[0]-i][start2[1]+i] for i in range(spaces2)])

def print_board():
    print "    a b c d e f g"
    for row in range(6):
        print str(6-row) + "  ",
        for space in gameboard[5-row]:
            print space,
        print

movenum = 1
movelist = open(argv[1]).read().splitlines()
for pair in movelist:
    move = place_move(pair[0],"X")
    print_board()
    if check_win(move,"X"):
        print "X won at move " + str(movenum)
        break
    move = place_move(pair[3],"O")
    print_board()
    if check_win(move,"O"):
        print "O won at move " + str(movenum)
        break
    movenum += 1
