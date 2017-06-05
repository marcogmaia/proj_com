#!/usr/bin/env python3
import curses
# from subprocess import call
import subprocess

empty = '#'
p1 = 'x'
p2 = 'o'

velha = [empty for i in range(9)]

def print_pos():
    print('posições:')
    for i in range(3):
        for j in range(3):
            print('{:5}'.format(i*3+j), end='')
        print()

def print_velha():
    print('game:')
    for i in range(3):
        print('    ', end='')
        for j in range(3):
            print('{:5}'.format(velha[i*3+j]), end='')
        print()

def get_pos():
    p = int(input())
    while p < 0 or p > 8:
        print('posição inválida. 0 <= p <= 8')
        p = int(input())
    return p

def print_game():
    subprocess.run(['clear'])
    print_pos()
    print_velha()

def check_equal(l):
    l = set(l)
    if empty in l or len(l) > 1:
        return False
    else:
        return True

def check_winner():
    l = []
    l.append([velha[i] for i in range(3)])
    l.append([velha[i+3] for i in range(3)])
    l.append([velha[i+6] for i in range(3)])
    l.append([velha[i*3] for i in range(3)])
    l.append([velha[i*3+1] for i in range(3)])
    l.append([velha[i*3+2] for i in range(3)])
    l.append([velha[4*i] for i in range(3)])
    l.append([velha[2*(i+1)] for i in range(3)])

    for i in l:
        if check_equal(i):
            return True

print_game()

# max number o turns (9)
turn = p1
used_pos = []
for i in range(9):
    print('\n "{}" escolha a posição:'.format(turn))

    p = get_pos()
    while p in used_pos:
        print('posição já ocupada')
        p = get_pos()
    used_pos.append(p)

    velha[p] = turn
    if check_winner():
        print_game()
        print('"{}" venceu.'.format(turn))
        break;

    print_game()
    turn = p2 if turn == p1 else p1

    if i == 8:
        print('deu Véia.')


