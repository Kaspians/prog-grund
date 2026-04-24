#!/usr/bin/env python3

# NOTE: [x] upg1 - skapa fil

# NOTE: [x] upg2 - Skapa class, constructor ...
class TicTacToeBoard:
    """
    Class about the logic of the game.
    """

    def __init__(self) -> None:
        # self._boardMatrix = self.defaultBoard

        self._boardMatrix = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]
        self.markerDict = {
            'row': [{}, {}, {}],
            'col': [{}, {}, {}],
            'diag': [{}, {}],
        }

    def get(self, row: int, col: int) -> str:
        """
        Returnerar värdet på plats row, col. Returvärdet är antingen
        'X', 'O', eller '-' för en ledig plats.
        row och col antas vara mellan 0 och 2.
        """
        cordStat = self._boardMatrix[row][col]
        return cordStat

    def is_empty(self, row: int, col: int) -> bool:
        """
        Returnerar `True` om platsen *row*, *col* är ledig, annars `False`.
        *row* och *col* antas vara mellan *0* och *2*.
        """
        cordStat = self._boardMatrix[row][col]
        if cordStat == '-':
            return True
        else:
            return False

    # NOTE: [x] upg3 - def place(), print_board(), is_full(), restart()

    def place(self, marker: str, row: int, col: int) -> bool:
        """
        Försöker placera *markören* `marker` på platsen `row`, `col`. Detta sker
        om platsen är ledig och *markören* är antingen **'X'** eller **'O'**.
        Returnerar `True` om så är fallet, annars `False`.
        `row` och `col` antas vara mellan *0* och *2*.
        """
        m = self._boardMatrix
        if self.is_empty(row, col):
            m[row][col] = marker
            return True
        else:  # NOTE: `else:` not needed, but becomes more readable
            print('ALREADY PLACED!')
            return False

    def print_board(self, printEmpty: bool) -> None:
        """
        Print **boardMatrix** in 3x3 *"grid"*, with their **symbol**
        **OPTIONAL**: if `is_empty` is *True*: print if they're **empty**.
        """
        print(f'cord [row/col]|symbol|is_empty:')
        for i in range(len(self._boardMatrix)):  # each row in matrix
            for j in range(len(self._boardMatrix[i])):  # each column in row $i
                print(f'[{i},{j}]', end=' ')
                print(f'{self.get(i, j)}', end=' ')
                if printEmpty:
                    print(f'{self.is_empty(i, j)}', end='')
                print('', end='\t')
            print('')

    def is_full(self) -> bool:
        """
        Returnerar `True` om brädet är *fullt* (all items != '-'), annars `False`.

        `lua`, *btw*
        .. code-block:: lua
        ---Same function in: `lua`, btw
        ---@param m table<table<str>>
        ---@return boolean
        for r,row in ipairs(m)
            for c, _ in ipairs(row)
                if not is_empty(r,c):
                    return false
                end
            end
        end
        return True
        """
        m = self._boardMatrix
        return all(
            not self.is_empty(r, c)
            for r, row in enumerate(m)  # INFO: for r,row in enumerate =
            #                           # index,content in ipairs(matrix) `lua`
            for c, _col in enumerate(row)  # (repeat for c, _col)
        )

    def restart(self) -> None:
        """
        Nollställer brädet. Alla platser blir *lediga*.
        """
        self._boardMatrix = [  # BUG: = self.defaultBoard did not work???
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]

    # TODO: [-] upg4 - def is_winner() - improve
    def is_winner(self, marker: str) -> bool:
        """
        If three of same `symbol` in a *row* (*hori*, *vert*, *diag*)

        # **SCRATCH**:
        * hori: check each m[row] if all are same
        * vert: check each m[row][n] if all are same
        * diag: check i++ and i--, for m[row][i] if all are same
        **USE** self.get() and self.is_empty()
        """
        b = self._boardMatrix
        m = self.markerDict

        def hori(row: int) -> None:
            dictRow = m['row'][row]
            dictRow[marker] = 0
            for c in range(len(b)):
                if self.get(row, c) == marker:
                    dictRow[marker] += 1
            # print(dictRow)  # PERF: temp

        def vert(col: int) -> None:
            dictCol = m['col'][col]
            dictCol[marker] = 0
            for r in range(len(b)):
                if self.get(r, col) == marker:
                    dictCol[marker] += 1
            # print(dictCol)  # PERF: temp

        def diag(dia: int) -> None:
            """
            * `0` = upLeft to downRight
            * `1` = upRight to downLeft
            """
            dictDiag = m['diag'][dia]
            dictDiag[marker] = 0
            for r in range(len(b)):
                if dia == 0:
                    c = r
                elif dia == 1:
                    c = 2 - r
                # print('diag cord', r, c)  # #TEST: temp
                if self.get(r, c) == marker:
                    dictDiag[marker] += 1
            # print(dictDiag)  # PERF: temp

        for i in range(len(b)):
            hori(i)
            vert(i)
            # print('row', row, m['row'][row])  # PERF: temp
            if int(m['row'][i][marker]) >= 3:
                return True
            # print('col', col, m['col'][col])  # PERF: temp
            if int(m['col'][i][marker]) >= 3:
                return True

        for dia in range(2):
            diag(dia)
            # print('diag', dia, m['diag'][dia])  # PERF: temp
            if int(m['diag'][dia][marker]) >= 3:
                return True

        # hori(int(input('Row nr? ')))

        # for i in m:
        #     print(i, m[i])  # PERF: temp

        return False  # ... if not True before
