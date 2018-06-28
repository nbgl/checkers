
#define variables
board = []
possible_moves = []


#use colorama to import colours for easier use
for number in range(10):
    if number == 1 or number == 3:
        board.append(['=',None,'BO',None,'BO',None,'BO',None,'BO','='])
    elif number == 7:
        board.append(['=',None,'WO',None,'WO',None,'WO',None,'WO','='])
    elif number == 2:
        board.append(['=','BO',None,'BO',None,'BO',None,'BO',None,'='])
    elif number == 6 or number == 8:
        board.append(['=','WO',None,'WO',None,'WO',None,'WO',None,'='])
    elif number == 4 or number == 5:
    #  REMOVE THE BO BELOW WHEN TESTING IS FINISHED!!!!!!
        board.append(['=',None,None,None,'BO',None,None,None,None,'='])
    elif number == 0 or number == 9:
        board.append(['=','==','==','==','==','==','==','==','==','='])
#printing the board
def print_board(board):
    testboard = board.copy()
    for row in testboard:
        for index in range(9):
            if row[index] == None:
                row[index] = '--'
        print (" ".join(row))



while True:
    print_board(board)
    coordIn = input('Enter the coordinates of which piece you would like to move:')
    #check if it is possible to move it first - not surrounded / blocked by other pieces
    x1Coord = int(coordIn[0])
    y1Coord = int(coordIn[-1])
    print (x1Coord)
    print (y1Coord)
    if board[y1Coord][x1Coord] != None and board[y1Coord][x1Coord] != 'BO':
        if board[y1Coord-1][x1Coord-1] == None:
            board.append([board[y1Coord-1][x1Coord-1]])
        elif board[y1Coord-1][x1Coord+1] == None:
            board.append([board[y1Coord-1][x1Coord+1]])
        elif board[y1Coord+1][x1Coord-1] == None:
            board.append([board[y1Coord+1][x1Coord-1]])
        elif board[y1Coord+1][x1Coord+1] == None:
            board.append([board[y1Coord+1][x1Coord+1]])
    else:
        print('Error - try again')
        continue

    #board[BoardIndex][boardIndex]
    coordOut = input('Enter where you would like to move it: ')
    x2Coord = int(coordOut[0])
    y2Coord = int(coordOut[-1])
    print (x2Coord)
    print(y2Coord)
    #check if it is possible to move it to that area
    xPossibleCoord = int(x2Coord)
    yPossibleCoord = int(y2Coord)

    if board[yPossibleCoord][xPossibleCoord] != None and board[yPossibleCoord][xPossibleCoord] != 'WO':
        if board[y2Coord-1][x2Coord-1] == None:
            possible_moves.append([possible_moves[y2Coord-1][x2Coord-1]])
        elif board[y2Coord-1][x2Coord+1] == None:
            possible_moves.append([possible_moves[y2Coord-1][x2Coord+1]])
        elif board[y1Coord+1][x2Coord-1] == None:
            possible_moves.append([possible_moves[y2Coord+1][x2Coord-1]])
        elif board[y2Coord+1][x2Coord+1] == None:
            possible_moves.append([possible_moves[y2Coord+1][x2Coord+1]])
    else:
        print('Error - try again')
        continue

    board[yPossibleCoord][xPossibleCoord] = "WO"
    board[y1Coord][x1Coord] = None

    print('Moved', coordIn,'to', coordOut)
    #insert AI's move





#array = [list1, list2,list3,list4,list5,list6,list7,list8]
#print in terminal
#'a'+str(1)

#whatever you put inside is printed to the console
#var = input()
#set variable equal to input
#enter commands after this


















#print(array)
#array[0].append('i')
#print(array)
