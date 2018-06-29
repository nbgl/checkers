
from copy import deepcopy

#define variables
list = []
from termcolor import cprint, colored
#cprint(colored("Hello", "grey", "on_white"))
board = []
possible_moves = []
surrounding =[]
game_end = False



#use colorama to import colours for easier use
def make_board(board):
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
            board.append(['4 ',None,None,None,None,None,None,None,None,' 4'])
        elif number == 5:
            board.append(['5 ',None,None,None,None,None,None,None,None,' 5'])
        elif number == 0 or number == 9:
            board.append([' ',' 1 ',' 2',' 3',' 4',' 5',' 6',' 7',' 8','  '])
#printing the boardminimax python checkers
def print_board(board):
    testboard = deepcopy(board)
    for row in testboard:
        for index in range(9):
            if row[index] == None:
                row[index] = '--'
            elif row[index] == "WO":
                row[index] = colored("WO", "red")
            elif row[index] == "BO":
                row[index] = colored("BO", "yellow")
    for row in testboard:
        print (' '.join(row))

print(""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |  ____  ____  | || |  _________   | || |     ______   | || |  ___  ____   | || |  _________   | || |  _______     | || |    _______   | |
| |   .' ___  |  | || | |_   ||   _| | || | |_   ___  |  | || |   .' ___  |  | || | |_  ||_  _|  | || | |_   ___  |  | || | |_   __ \    | || |   /  ___  |  | |
| |  / .'   \_|  | || |   | |__| |   | || |   | |_  \_|  | || |  / .'   \_|  | || |   | |_/ /    | || |   | |_  \_|  | || |   | |__) |   | || |  |  (__ \_|  | |
| |  | |         | || |   |  __  |   | || |   |  _|  _   | || |  | |         | || |   |  __'.    | || |   |  _|  _   | || |   |  __ /    | || |   '.___`-.   | |
| |  \ `.___.'\  | || |  _| |  | |_  | || |  _| |___/ |  | || |  \ `.___.'\  | || |  _| |  \ \_  | || |  _| |___/ |  | || |  _| |  \ \_  | || |  |`\____) |  | |
| |   `._____.'  | || | |____||____| | || | |_________|  | || |   `._____.'  | || | |____||____| | || | |_________|  | || | |____| |___| | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'

""")

#insert bigger loop for AI
while True:
    make_board(board)
    while not game_end:
        while not game_end:
            for row in board:
                if "WO" in row:
                    break
            else:
                game_end = True
            if not game_end:

                print_board(board)
                print ("Player WO's turn")
                coordIn = input('Enter the coordinates of which piece you would like to move:')
                #check if it is possible to move it first - not surrounded / blocked by other pieces
                x1Coord = int(coordIn[0])
                y1Coord = int(coordIn[-1])
                print (x1Coord)
                print (y1Coord)
                if board[y1Coord][x1Coord] == 'WO':
                    if board[y1Coord+1][x1Coord-1] == None:
                        surrounding.append(board[y1Coord+1][x1Coord-1])
                    elif board[y1Coord+1][x1Coord+1] == None:
                        surrounding.append(board[y1Coord+1][x1Coord+1])
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
                        board[yPossibleCoord][xPossibleCoord] = "WO"
                                    #depending on where you have moved, check if you jumped two spaces up or two spaces down in either direction (killed an enemy)
                                    #if you have, set the possiblecoords to None

                        board[y1Coord][x1Coord] = None
                        break
                    elif abs(x1Coord - xPossibleCoord) == 1 and abs(y1Coord - yPossibleCoord) == 1:

                        if board[yPossibleCoord][xPossibleCoord] == None:
                            board[yPossibleCoord][xPossibleCoord] = "WO"
                        #depending on where you have moved, check if you jumped two spaces up or two spaces down in either direction (killed an enemy)
                        #if you have, set the possiblecoords to None

                            board[y1Coord][x1Coord] = None


                            print('Moved', coordIn,'to', coordOut)
                            break
                        else:
                            print('Error - try again')
                            continue
                    else:
                        print('Error - try again')
                        continue

                else:
                    print('Error - try again')
                    continue
        #insert AI / other player
        while not game_end:
            for row in board:
                if "BO" in row:
                    break
            else:
                game_end = True
            if not game_end:
                print_board(board)
                print ("Player BO's turn")
                coordIn = input('Enter the coordinates of which piece you would like to move:')
                #check if it is possible to move it first - not surrounded / blocked by other pieces
                x1Coord = int(coordIn[0])
                y1Coord = int(coordIn[-1])
                print (x1Coord)
                print (y1Coord)
                if board[y1Coord][x1Coord] == 'BO':
                    if board[y1Coord-1][x1Coord-1] == None:
                        surrounding.append(board[y1Coord-1][x1Coord-1])
                    elif board[y1Coord-1][x1Coord+1] == None:
                        surrounding.append(board[y1Coord-1][x1Coord+1])
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
                    if board[yPossibleCoord][xPossibleCoord] == 'WO':
                        board[yPossibleCoord][xPossibleCoord] = "BO"
                                    #depending on where you have moved, check if you jumped two spaces up or two spaces down in either direction (killed an enemy)
                                    #if you have, set the possiblecoords to None

                        board[y1Coord][x1Coord] = None
                        break
                    elif abs(x1Coord - xPossibleCoord) == 1 and abs(y1Coord - yPossibleCoord) == 1:

                        if board[yPossibleCoord][xPossibleCoord] == None:
                            board[yPossibleCoord][xPossibleCoord] = "BO"
                        #depending on where you have moved, check if you jumped two spaces up or two spaces down in either direction (killed an enemy)
                        #if you have, set the possiblecoords to None

                            board[y1Coord][x1Coord] = None


                            print('Moved', coordIn,'to', coordOut)
                            break
                        else:
                            print('Error - try again')
                            continue

                else:
                    print('Error - try again')
                    continue
    print("""   ______ ___     __  ___ ______   ____  _    __ ______ ____
      / ____//   |   /  |/  // ____/  / __ \| |  / // ____// __ \
     / / __ / /| |  / /|_/ // __/    / / / /| | / // __/  / /_/ /
    / /_/ // ___ | / /  / // /___   / /_/ / | |/ // /___ / _, _/
    \____//_/  |_|/_/  /_//_____/   \____/  |___//_____//_/ |_|


    """)
    input('Press enter to play again.')
    game_end = False







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
