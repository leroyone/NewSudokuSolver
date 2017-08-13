#! /usr/bin/python3

from sudokuClass import *
import subprocess as sp

def clear():
    sp.call('clear', shell=True)

def moveForward(a,b):
    if b == 8:
        a += 1
        b = 0
    else:
        b += 1
    return a,b
    

def setupSudoku(grid):
    clear()
    a,b = 0,0
    while a <= 8 and b <= 8:
        grid.insertNumber(a,b,'_')
        print('Type number at ' + str(a) + ',' + str(b) + '. (Enter) if blank. (b) to go back.\n')
        grid.printAcross()
        x = input()
        if x == '':
            grid.insertNumber(a,b,'-')
            a,b = moveForward(a,b)
            clear()
        elif x in ('123456789') and int(x) in range(1,10):
            if checker(a,b,x,grid):
                grid.insertNumber(a,b,x)
                a,b = moveForward(a,b)
                clear()
            else:
                clear()
                input('Invalid input. Please try again.\n')
        elif x == 'b' or x == 'B':
            if a == 0 and b == 0:
                clear()
                input('Can not go back. Already at the start!\n')
            elif b == 0:
                grid.insertNumber(a,b,'-')
                a -= 1
                b = 8
                clear()
            else:
                grid.insertNumber(a,b,'-')
                b -= 1
                clear()
        else:
            clear()
            input('Invalid input. Please try again.\n')
                
def checker(a,b,x,grid):
    thisSquare,cordB = grid.squareConv(a,b)
    if x not in grid.across[a] and x not in grid.down[b] and x not in grid.square[thisSquare]:
        return True
    else:
        return False

grid = Sudoku()
setupSudoku(grid)