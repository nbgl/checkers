
#define variables
list = []
from pynput.keyboard import Key, Controller


keyboard = Controller()
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
                row[index] = 'Na'
        print (" ".join(row))

print_board(list)

#keyboard.press(Key.space)
#keyboard.release(Key.space)
#keyboard.press('a')
#keyboard.release('a')






#array = [list1, list2,list3,list4,list5,list6,list7,list8]
#print in terminal
#'a'+str(1)














#print(array)
#array[0].append('i')
#print(array)
