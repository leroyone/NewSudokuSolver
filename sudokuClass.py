#! /usr/bin/python3

class Sudoku:
    '''
    a Sudoku grid to manipulate and search.
    initially blank
    '''

    def __init__(self):
        def blankGrid():
            blanky = []
            for each in range(9):
                column = []
                for every in range(9):
                    empty = '-'
                    column.append(empty)
                blanky.append(column)
            return blanky

        self.down = blankGrid()
        self.across = blankGrid()
        self.square = blankGrid()

    def printAcross(self):
        '''
        prints to screen the across grid
        '''
        count = 0
        for each in self.across:
            if count%3 == 0 and count != 0:
                print()
            print(' '.join(each[:3]), end='')
            print('  ', end='')
            print(' '.join(each[3:6]), end='')
            print('  ', end='')
            print(' '.join(each[6:]))
            count += 1

    def printDown(self):
        '''
        prints to screen the down grid
        '''
        for column in range(9):
            for row in range(9):
                print(self.down[row][column], end=' ')
                if row in (2,5):
                    print(' ', end='')
                if row == 8:
                    print()
            if column in (2,5):
                print()

    def printSquare(self):
        '''
        prints to screen the square grid
        '''
        count = 0
        for eachA in range(3):
            for everyA in range(3):
                for each in range(3):
                    for every in range(3):
                        if count%27 == 0 and count != 0:
                            print()
                        if count%9 == 0 and count != 0:
                            print()
                        elif count%3 == 0 and count !=0:
                            print(' ', end='')
                        count+=1
                        print(self.square[each+(eachA*3)][every+(everyA*3)], end=' ')
        print()

    def printSquare2(self):
        '''
        prints to screen the square grid
        '''
        count = 0
        while len(self.square) != 0:
            for each in range(3):
                for every in range(3):
                    if count%27 == 0 and count != 0:
                        print()
                    if count%9 == 0 and count != 0:
                        print()
                    elif count%3 == 0 and count !=0:
                        print(' ', end='')
                    count+=1
                    print(self.square[each].pop(0), end=' ')
            while len(self.square) != 0 and len(self.square[0]) == 0:
                self.square.pop(0)
        print()

    def squareConv(self,cordA,cordB):
        '''
        input: across grid coodinates
        return: square grid coordinates
        '''
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
        aSquare = squareSet(cordA)*3+squareSet(cordB)
        bSquare = (cordA%3)*3+cordB%3
        return aSquare,bSquare

    def insertNumber(self,a,b,numberToInsert):
        '''
        a and b: int coordinates
        numberToInsert: str
        inserts th number in all three grids
        '''
        numberToInsert = str(numberToInsert)
        self.across[a][b]=numberToInsert
        self.down[b][a]=numberToInsert
        e,f = self.squareConv(a,b)
        self.square[e][f]=numberToInsert