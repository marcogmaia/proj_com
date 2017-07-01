#!/usr/bin/env python3
import argparse
import sys
import socket
import pickle # for veia structure serialization.
# import curses

import subprocess

class my_parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)

class veia():
    board = [i+1 for i in range(9)]
    board = {i: i for i in board}
    board['plays'] = 0
    board['winner'] = None
    player1 = 'x'
    player2 = 'o'
    
    def __init__(self, player):
        self.player = player
        self.board = veia.board
        self.end = False

    def check(self, p):
        if ((self.board[1] == self.board[2] == self.board[3] == p) or
            (self.board[4] == self.board[5] == self.board[6] == p) or
            (self.board[7] == self.board[8] == self.board[9] == p) or
            (self.board[1] == self.board[4] == self.board[7] == p) or
            (self.board[2] == self.board[5] == self.board[8] == p) or
            (self.board[3] == self.board[6] == self.board[9] == p) or
            (self.board[1] == self.board[5] == self.board[9] == p) or
            (self.board[3] == self.board[5] == self.board[7] == p)):
            self.board['winner'] = p
            self.end = True

        elif self.board['plays'] == 9:
            self.end = True


    def make_a_move(self):
        pos = -1
        while pos < 1 or 9 < pos:
            pos = int(input())
        self.board[pos] = self.player
        self.board['plays'] += 1

    def send_board(self):
        return pickle.dumps(self.board, -1)

    def receive_board(self, bin_board):
        self.board = pickle.loads(bin_board)

    def print_board(self):
        subprocess.run('clear')
        print('positions:')
        for i in reversed(range(3)):
            k = i*3
            print(self.board[k+1], self.board[k+2], self.board[k+3])

    def result_message(self):
        other_player = veia.player1 if self.player == veia.player2 else veia.player1
        if self.board['winner'] == self.player:
            print('Ganhou poar')
        elif self.board['winner'] == other_player:
            print('Sifudeu')
        else:
            print('Deu véia')

    def ended(self):
        return self.end


def get_machine_lan_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    machine_lan = s.getsockname()
    s.close()
    return machine_lan[0]

def main():
    # parser = argparse.ArgumentParser()
    parser = my_parser(description='A véia game via sockets in python.')
    parser.add_argument('-c', '--connect', metavar='address',
        help='address to connect to.', type=str, default='server')
    args = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = get_machine_lan_address()
    port = 5553
    quit = False

    if args.connect == 'server':
        try:
            print('local ip: {}'.format(host))
            s.bind((host, port))
            s.listen(1)
            connection, addr = s.accept()

            # game starts here
            game = veia(veia.player1)
            while not game.ended():
                game.print_board()
                print('Your turn: ', end='')
                game.make_a_move()
                game.check(veia.player1)
                game.print_board()
                connection.send(game.send_board())
                if not game.ended():
                    game.receive_board(connection.recv(4096))
                    game.print_board()
                    game.check(veia.player2)
            game.result_message()            
        except KeyboardInterrupt as e:
            print(e)
        finally:
            s.close()
            try:
                connection.close()
            except Exception as e:
                # print(e)
                pass

    else: # "client"
        try:
            connection = socket.create_connection((args.connect, port))

            # game starts here
            game = veia(veia.player2)
            while not game.ended():
                game.print_board()
                game.receive_board(connection.recv(4096))
                game.check(veia.player1)
                game.print_board()
                if not game.ended():
                    print('Your turn: ', end='')
                    game.make_a_move()
                    game.check(veia.player2)
                    game.print_board()
                    connection.send(game.send_board())
            game.result_message()                   
        except socket.error as e:
            print(e)
        finally:
            try:
                connection.close()
            except Exception as e:
                # print(e)
                pass


if __name__ == '__main__':
    main()
