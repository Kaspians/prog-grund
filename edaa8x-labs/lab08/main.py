#!/usr/bin/env python3

from board import TicTacToeBoard

# NOTE: [x] upg6 - __name__ == __main__
if __name__ == '__main__':

    def Main() -> None:
        """
        `Main()` run until board `is_full`
        - 1. place
        - 2. print board
        - 3. restart
        - <None>. quit

        .. code-block:: markdown
        **markdown** like this, _btw_
        """
        t = TicTacToeBoard()
        t.print_board(False)
        turn = 0

        while not t.is_full():
            # t.print_board(False) # TEST: spammy?
            if turn % 2 == 0:
                marker = 'X'
            else:
                marker = 'O'
            print()
            ask = input(f"""
        Marker's turn: > {marker} <

            What do you want to do?
            - 1. place
            - 2. print board
            - 3. restart
            - <None>. quit
            """)
            if ask == '1':
                rowcol = input('row/col? (format: [xy]) ')
                if len(rowcol) == 2:
                    row, col = rowcol[0], rowcol[1]
                    if row in ('0', '1', '2') and col in ('0', '1', '2'):
                        t.place(marker, int(row), int(col))
                        t.print_board(False)
                        if t.is_winner(marker):
                            print(marker, 'WIN')
                            break
                        turn += 1
                    else:
                        print('\n    0 <= int <= 2')
                else:
                    print('\n    only 2 int (xx)!')
            elif ask == '2':
                t.print_board(True)
            elif ask == '3':
                t.restart()
                t.print_board(False)
            elif ask == '':
                break
            else:
                print(f"""
                Huh?
                Wtf is: "{ask}"
                """)

        t.is_full()
        print('is_full() =', t.is_full())

    Main()
    # b = TicTacToeBoard()
    # b.place('X', 0, 0)
    # b.print_board(False)
