#!/usr/bin/env python3
import curses
import locale

locale.setlocale(locale.LC_ALL, '')


def main(stdscr):

    # Init:
    curses.noecho()
    curses.cbreak()

    if curses.has_colors():
        curses.start_color()

    stdscr.keypad(True)
    stdscr.clear()
    
    stdscr.refresh()

    # derive window from stdscr
    board = stdscr.derwin(7, 7, 2, 10)
    board.move(1, 1)
    # board.mvderwin(3, 4)
    table = board.derwin(5, 5, 1, 1)

    i, j = pos = [1, 1]
    mov_keys = [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]

    # table_pos = [ (1, 1),
    #               (1, 3),
    #               (1, 5),
    #               (3, 1),
    #               (3, 3),
    #               (3, 5),
    #               (5, 1),
    #               (5, 3),
    #               (5, 5)]
    l = [1, 3, 5]
    table_pos = [(i, j) for i in l for j in l]
    table_dict = {table_pos[i]: i for i in range(len(table_pos))}

    ch = 0


    def arrow_move(pos):
        if ch in mov_keys:

            i, j = pos

            if ch == curses.KEY_UP:
                i -= 2
            elif ch == curses.KEY_DOWN:
                i += 2

            elif ch == curses.KEY_LEFT:
                j -= 2
            elif ch == curses.KEY_RIGHT:
                j += 2

            max_y, max_x = board.getmaxyx()

            if i < 0:
                i = 1
            elif j < 0:
                j = 1
            elif i >= max_y:
                i = max_y-2
            elif j >= max_x:
                j = max_x-2
            board.move(i, j)

            pos[0] = i
            pos[1] = j

            board.refresh()
            
    def print_board(i, j):
        # board.mvderwin(i, j)
        board.box()

        table.addch(1, 0, curses.ACS_HLINE)
        table.addch(1, 2, curses.ACS_HLINE)
        table.addch(1, 4, curses.ACS_HLINE)

        table.addch(3, 0, curses.ACS_HLINE)
        table.addch(3, 2, curses.ACS_HLINE)
        table.addch(3, 4, curses.ACS_HLINE)

        table.addch(1, 1, curses.ACS_SSSS)
        table.addch(1, 3, curses.ACS_SSSS)
        table.addch(3, 1, curses.ACS_SSSS)
        table.addch(3, 3, curses.ACS_SSSS)
        
        table.addch(0, 1, curses.ACS_VLINE)
        table.addch(2, 1, curses.ACS_VLINE)
        table.addch(4, 1, curses.ACS_VLINE)

        table.addch(0, 3, curses.ACS_VLINE)
        table.addch(2, 3, curses.ACS_VLINE)
        table.addch(4, 3, curses.ACS_VLINE)

        board.refresh()
        # table.refresh()

    board.move(1, 1)
    print_board(4, 8)

    pposwin = stdscr.derwin(4, 6, 2, 17)
    pposwin.box()
    pposwin.refresh()
    poswin = pposwin.derwin(2, 4, 1, 1)
    board.refresh()

    # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # stdscr.bkgd(' ', curses.color_pair(5))


    # game loop
    while ch != 'q':


        # poswin.deleteln()
        poswin.move(0, 0); poswin.clrtoeol()
        arrow_move(pos)
        y, x = board.getyx()
        poswin.addstr(0, 0, str(y)+', '+str(x))
        poswin.refresh()
        board.refresh()

        ch = stdscr.get_wch()
        if ch == '\n' and (y, x) in table_pos:
            poswin.addch(1, 0, str(table_dict[(y, x)]))
            poswin.refresh()
            board.addch(y, x, 'x')
            board.move(y, x)
            board.refresh()



if __name__=='__main__':
    curses.wrapper(main)
