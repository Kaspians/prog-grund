#!/usr/bin/env python3

from board import TicTacToeBoard
from window_tk import TicTacToeApp

# NOTE: [x] upg6 - __name__ == __main__
if __name__ == '__main__':

    def Main() -> None:
        """
        `Main()` run until board `is_full`
        - [xy](int)         => `place()`
        - 'exit'(string)    => `break`
        - 'restart'(string) => `restart()`

        .. code-block:: markdown
        **markdown** like this, _btw_
        """
        t = TicTacToeBoard()
        t.print_board(False)
        turn = 0
        tk = TicTacToeApp(t)

        while not t.is_full():
            if turn % 2 == 0:
                marker = 'X'
            else:
                marker = 'O'
            print()
            ask = input(f"""
        Marker's turn: > {marker} <

            What do you want to do? Type:
            - [xy](int)         => `place(xy[0], xy[1])`
            - 'exit'(string)    => `break`
            - 'restart'(string) => `restart()`
            """)
            if len(ask) == 2:
                row, col = ask[0], ask[1]
                if row in ('0', '1', '2') and col in ('0', '1', '2'):
                    t.place(marker, int(row), int(col))
                    t.print_board(False)
                    if t.is_winner(marker):
                        print(marker, 'WIN')
                        break
                    turn += 1
                else:
                    print('\n    0 <= int <= 2')
            elif ask == 'exit':
                break
            elif ask == 'restart':
                t.restart()
                t.print_board(False)
            else:
                print('\n\t Only 2-char-int(xy), "exit", or "restart"')

        t.is_full()
        print('is_full() =', t.is_full())

    Main()
