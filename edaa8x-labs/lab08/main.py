#!/usr/bin/env python3

from board import TicTacToeBoard
from window_tk import TicTacToeApp

# NOTE: [x] upg6 - __name__ == __main__
if __name__ == '__main__':

    def Main() -> None:
        """
        `Main()` run until board `is_full`
        - <xy>(int)         => `place()`
        - "q"uit(string)    => `break`
        - "r"estart(string) => `restart()`

        .. code-block:: markdown
        **markdown** like this, _btw_
        """
        t = TicTacToeBoard()
        t.print_board(False)
        turn = 0

        gui_or_cli = input('<g>ui or <c>li? ')
        if gui_or_cli == 'g':
            tk = TicTacToeApp(t)
        elif gui_or_cli == 'c':
            while not t.is_full():
                if turn % 2 == 0:
                    marker = 'X'
                else:
                    marker = 'O'
                print()
                ask = input(f"""
            Marker's turn: > {marker} <

                What do you want to do? Type:
                - [xy](int)           => `place()`
                - ['q']uit(string)    => `break`
                - ['r']estart(string) => `restart()`
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
                elif ask == 'q':
                    break
                elif ask == 'r':
                    t.restart()
                    t.print_board(False)
                else:
                    print('\n\t Only [xy](2-char-int, cords), "q"(uit), or "r"(estart)')

                t.is_full()
                print('is_full() =', t.is_full())
        else:
            print('What? Try again...')

    Main()
