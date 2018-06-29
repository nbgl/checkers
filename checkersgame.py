
from copy import deepcopy


#define variables
board = []
possible_moves = []
surrounding =[]



#use colorama to import colours for easier use
for number in range(10):
    if number == 1:
        board.append(['1 ',None,'BO',None,'BO',None,'BO',None,'BO',' 1'])
    elif number == 3:
        board.append(['3 ',None,'BO',None,'BO',None,'BO',None,'BO',' 3'])
    elif number == 7:
        board.append(['7 ',None,'WO',None,'WO',None,'WO',None,'WO',' 7'])
    elif number == 2:
        board.append(['2 ','BO',None,'BO',None,'BO',None,'BO',None,' 2'])
    elif number == 6:
        board.append(['6 ','WO',None,'WO',None,'WO',None,'WO',None,' 6'])
    elif number == 8:
        board.append(['8 ','WO',None,'WO',None,'WO',None,'WO',None,' 8'])
    elif number == 4:
    #  REMOVE THE BO BELOW WHEN TESTING IS FINISHED!!!!!!
        board.append(['4 ',None,None,None,'BO',None,None,None,None,' 4'])
    elif number == 5:
        #  REMOVE THE BO BELOW WHEN TESTING IS FINISHED!!!!!!
        board.append(['5 ',None,None,None,'BO',None,None,None,None,' 5'])
    elif number == 0 or number == 9:
        board.append([' ',' 1 ',' 2',' 3',' 4',' 5',' 6',' 7',' 8','  '])
#printing the board
def print_board(board):
    testboard = deepcopy(board)
    for row in testboard:
        for index in range(9):
            if row[index] == None:
                row[index] = '--'
        print (" ".join(row))


#insert bigger loop for AI
while True:
    print_board(board)
    coordIn = input('Enter the coordinates of which piece you would like to move:')
    #check if it is possible to move it first - not surrounded / blocked by other pieces
    x1Coord = int(coordIn[0])
    y1Coord = int(coordIn[-1])
    print (x1Coord)
    print (y1Coord)
    if board[y1Coord][x1Coord] == 'WO':
        if board[y1Coord+1][x1Coord-1] == None:
            surrounding.append([board[y1Coord+1][x1Coord-1]])
        elif board[y1Coord+1][x1Coord+1] == None:
            surrounding.append([board[y1Coord+1][x1Coord+1]])
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
    if x1Coord != xPossibleCoord and y1Coord != yPossibleCoord:
        if board[yPossibleCoord][xPossibleCoord] == 'BO':
            if board[y1Coord+1][x2Coord-1] == None:
                possible_moves.append([possible_moves[y2Coord+1][x2Coord-1]])
            elif board[y2Coord+1][x2Coord+1] == None:
                possible_moves.append([possible_moves[y2Coord+1][x2Coord+1]])

        elif board[yPossibleCoord][xPossibleCoord] == None:
            board[yPossibleCoord][xPossibleCoord] = "WO"
            #depending on where you have moved, check if you jumped two spaces up or two spaces down in either direction (killed an enemy)
            #if you have, set the possiblecoords to None

            board[y1Coord][x1Coord] = None


            print('Moved', coordIn,'to', coordOut)
        else:
            print('Error - try again')
            continue
    else:
        print('Error - try again')
        continue
    #insert AI









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
