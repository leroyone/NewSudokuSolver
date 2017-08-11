#! /usr/bin/python3.2

def blankGrid():
    '''
    returns a 9x9 grid
    '''
    down = []
    for each in range(9):
        column = []
        for every in range(9):
            empty = '-'
            column.append(empty)
        down.append(column)
    return down

def printAcross(across):
    '''
    prints to screen the across grid
    '''
    count = 0
    for each in across:
        if count%3 == 0 and count != 0:
            print()
        print(' '.join(each[:3]), end='')
        print('  ', end='')
        print(' '.join(each[3:6]), end='')
        print('  ', end='')
        print(' '.join(each[6:]))
        count += 1

def printDown(down):
    '''
    prints to screen the down grid
    '''
    for column in range(9):
        for row in range(9):
            print(down[row][column], end=' ')
            if row in (2,5):
                print(' ', end='')
            if row == 8:
                print()
        if column in (2,5):
            print()

def printSquare(square):
    '''
    prints to screen the square grid
    '''
    count = 0
    while len(square) != 0:
        for each in range(3):
            for every in range(3):
                if count%27 == 0 and count != 0:
                    print()
                if count%9 == 0 and count != 0:
                    print()
                elif count%3 == 0 and count !=0:
                    print(' ', end='')
                count+=1
                print(square[each].pop(0), end=' ')
        while len(square) != 0 and len(square[0]) == 0:
            square.pop(0)

def downConv(cordA,cordB):
    '''
    takes Across grid coordinates and returns Down grid coordinates
    '''
    return cordB,cordA

def squareSet(theNumber):
    '''
    theNumber = int
    return: int for which range theNumber is in 
    '''
    if theNumber in (0,1,2):
        return 0
    if theNumber in (3,4,5):
        return 1
    if theNumber in (6,7,8):
        return 2

def squareConv(cordA,cordB):
    '''
    input: across grid coodinates
    return: square grid coordinates
    '''
    aSquare = squareSet(cordA)*3+squareSet(cordB)
    bSquare = (cordA%3)*3+cordB%3
    return aSquare,bSquare

def insertNumber(a,b,numberToInsert):
    '''
    a and b: int coordinates
    numberToInsert: str
    inserts th number in all three grids
    '''
    across[a][b]=numberToInsert
    down[b][a]=numberToInsert
    e,f = squareConv(a,b)
    square[e][f]=numberToInsert

def main():
    insertNumber(5,6,'9')

    printAcross(across)
    print('~~~~~~~~~~~~~~~~~~~')
    printDown(down)
    print('~~~~~~~~~~~~~~~~~~~')
    printSquare(square)
    print()

down = blankGrid()
across = blankGrid()
square = blankGrid()

main()