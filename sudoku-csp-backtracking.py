import time

start = time.time()


class SdkWithBT():

    def __init__(self, states: [], length, subColLen, subRowLen):

        self.states = states
        self.length = length
        self.subColLen = subColLen
        self.subRowLen = subRowLen
        self.scope = {}
        self.changeScope()

    def consistencyCheck(self, thisnum, row, col) -> bool:
        for i in range(self.length):
            if self.states[row][i] == thisnum:
                return False
        for j in range(self.length):
            if self.states[j][col] == thisnum:
                return False
        rowInit = (row // self.subRowLen) * self.subRowLen
        colInit = (col // self.subColLen) * self.subColLen
        for i in range(rowInit, rowInit + self.subRowLen):
            for j in range(colInit, colInit + self.subColLen):
                if self.states[i][j] == thisnum:
                    return False
        return True

    def changeScope(self):
        self.scope = {}
        vars = []

        for i in range(self.length):
            for j in range(self.length):
                if self.states[i][j] == 0:
                    vars = []
                    for k in range(1, self.length + 1):
                        if self.consistencyCheck(k, i, j):
                            vars.append(k)

                    if len(vars) >= 1:
                        self.scope[(i, j)] = vars

    def findFirstEmpty(self) -> ():
        for i in range(self.length):
            for j in range(self.length):
                if self.states[i][j] == 0:
                    return (i, j)
        return None, None

    def EndCheck(self) -> bool:

        for i in range(self.length):
            for j in range(self.length):

                if self.states[i][j] == 0:
                    return False

        return True

    def BT(self) -> bool:
        y, x = self.findFirstEmpty()

        if y is None or x is None:
            return True

        for k in range(1, self.length + 1):
            if self.consistencyCheck(k, y, x):
                self.states[y][x] = k
                if self.BT():
                    return True
                self.states[y][x] = 0
        return False

    def boardPrint(self):

        for i in range(self.length):
            print('# ', end='')
            if i != 0 and i % self.subRowLen == 0:
                for k in range(self.length):
                    print(' # ', end='')
                    if (k + 1) < self.length and (k + 1) % self.subColLen == 0:
                        print(' * ', end='')
                print(' #')
                print('# ', end='')
            for j in range(self.length):
                if j != 0 and j % self.subColLen == 0:
                    print(' # ', end='')
                digit = str(self.states[i][j]) if len(str(self.states[i][j])) > 1 else ' ' + str(self.states[i][j])
                print('{0} '.format(digit), end='')
            print(' #')


def main():
    inpboard = [0, 0, 0, 0, 0, 0, 2, 0, 0,
                0, 8, 0, 0, 0, 7, 0, 9, 0,
                6, 0, 2, 0, 0, 0, 5, 0, 0,
                0, 7, 0, 0, 6, 0, 0, 0, 0,
                0, 0, 0, 9, 0, 1, 0, 0, 0,
                0, 0, 0, 0, 2, 0, 0, 4, 0,
                0, 0, 5, 0, 0, 0, 6, 0, 3,
                0, 9, 0, 4, 0, 0, 0, 7, 0,
                0, 0, 6, 0, 0, 0, 0, 0, 0]
    length = 9
    subColLen = 3
    subRowLen = 3

    initial_state = []
    row = []
    counter = 0
    for i in inpboard:
        counter += 1
        row.append(i)
        if counter >= length:
            initial_state.append(row)
            row = []
            counter = 0

    board = SdkWithBT(initial_state, length, subColLen, subRowLen)
    board.BT()
    print('\nSolution for  this board:')
    board.boardPrint()
    print()
    print("--- %s seconds ---" % (time.time() - start))


if __name__ == "__main__": main()
