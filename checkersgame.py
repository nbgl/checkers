#define variables
list = []

#use colorama to import colours for easier use
for number in range(1,9):
    if number == 1 or number == 3:
        list.append([None,'BO',None,'BO',None,'BO',None,'BO'])
    elif number == 7:
        list.append([None,'WO',None,'WO',None,'WO',None,'WO'])
    elif number == 2:
        list.append(['BO',None,'BO',None,'BO',None,'BO',None])
    elif number == 6 or number == 8:
        list.append(['WO',None,'WO',None,'WO',None,'WO',None])
    elif number == 4 or number == 5:
        list.append([None,None,None,None,None,None,None,None])
#printing the board
def print_board(board):
    testboard = board.copy()
    for row in testboard:
        for index in range(8):
            if row[index] == None:
                row[index] = '--'
        print (" ".join(row))

print_board(list)

#def process_input():

while True:
    coordIn = input('Enter the coordinates of which piece you would like to move:')
    #check if it is possible to move it first - not surrounded / blocked by other pieces
    x1Coord = coordIn[0]
    y1Coord = coordIn[-1]
    print (x1Coord)
    print(y1Coord)
    if list[y1Coord][x1Coord] != None and list[y1Coord][x1Coord] != 'BO':
        if list[y1Coord-1][x1Coord-1] = None:
            list.append([list[y1Coord-1][x1Coord-1]])
        elif list[y1Coord-1][x1Coord+1] = None:
            list.append([list[y1Coord-1][x1Coord+1]])
        elif list[y1Coord+1][x1Coord-1] = None:
            list.append([list[y1Coord+1][x1Coord-1]])
        elif list[y1Coord+1][x1Coord+1] = None:
            list.append([list[y1Coord+1][x1Coord+1]])
        else:
            print('Error - try again')
            continue
    #remember
    if [x1Coord] = 7


    if



#board[BoardIndex][ListIndex]
coordOut = input('Enter where you would like to move it: ')
x2Coord = coordIn[0]
y2Coord = coordIn[-1]
print (x2Coord)
print(y2Coord)
#check if it is possible to move it to that area
print('Moved', coordIn,'to', coordOut)




#whatever you put inside is printed to the console
#var = input()
#set variable equal to input
#enter commands after this


















#print(array)
#array[0].append('i')
#print(array)
