import random
import time
import os

random.seed(random.randrange(123456789))

alfabet = "ABCDEFGHIJKLMNOPRSTUWYZ"

def losuj_literke():
    rand_index = random.randint(0, len(alfabet)-1)
    wylosowana_literka = alfabet[rand_index]
    return wylosowana_literka

def losuj(zakres):
    return random.randrange(zakres)

def inicjalizacja_board(board):
    pass

def drukuj_board(board):
    os.system('cls')
    for wiersz in board:
        print(wiersz)
    print('\n')

def losuj_pary(ilosc):
    rodzaje_kart = []
    wylosowana_literka = alfabet[random.randrange(len(alfabet)-1)]

    for i in range(int(ilosc)):
        while(wylosowana_literka in rodzaje_kart):
            wylosowana_literka = losuj_literke()
        rodzaje_kart.append(wylosowana_literka)
    return rodzaje_kart

def generate_board(height, width):
    board = [["-" for i in range(width)] for i in range(height)]
    return board

def wolne_miejsca(board):
    for wiersz in board:
        for kolumna in wiersz:
            if kolumna=='-':
                return True
    return False

def losuj_karty(height, width):
    ilosc_par = (height * width) / 2
    rodzaje_kart = losuj_pary(ilosc_par)
    return rodzaje_kart

def wolne_pole(board, x, y):
    if board[x][y] == '-':
        return True
    return False
    
def uzupelnij_board(height, width, board, karty):
    for karta in karty:
        for i in range(2):
            x=0
            y=0
            while(wolne_miejsca(board) and not wolne_pole(board, x, y)):
                x=losuj(width)
                y=losuj(height)
            board[x][y]=karta
     
height = 2
width = 2
board = generate_board(height, width)
karty = losuj_karty(height, width)
uzupelnij_board(height, width, board, karty)
# drukuj_board(board)
board_uzytkownika = generate_board(height, width)
while wolne_miejsca(board_uzytkownika):
    drukuj_board(board_uzytkownika)
    wspolrzednex = int(input('podaj wspolrzendna x '))
    wspolrzedney = int(input('podaj wspolrzendna y '))
    board_uzytkownika[wspolrzedney-1][wspolrzednex-1]=board[wspolrzedney-1][wspolrzednex-1]
    drukuj_board(board_uzytkownika)
    wspolrzednex2 = int(input('podaj wspolrzendna x '))
    wspolrzedney2 = int(input('podaj wspolrzendna y '))
    board_uzytkownika[wspolrzedney2-1][wspolrzednex2-1]=board[wspolrzedney2-1][wspolrzednex2-1]
    drukuj_board(board_uzytkownika)
    time.sleep(2)
    if board_uzytkownika[wspolrzedney2-1][wspolrzednex2-1]==board_uzytkownika[wspolrzedney-1][wspolrzednex-1]:
        board_uzytkownika[wspolrzedney2-1][wspolrzednex2-1]='*'
        board_uzytkownika[wspolrzedney-1][wspolrzednex-1]='*'
    if board_uzytkownika[wspolrzedney2-1][wspolrzednex2-1]!=board_uzytkownika[wspolrzedney-1][wspolrzednex-1]:
        board_uzytkownika[wspolrzedney2-1][wspolrzednex2-1]='-'
        board_uzytkownika[wspolrzedney-1][wspolrzednex-1]='-'
for i in range(1,6):
    os.system('cls')
    print(6-i)
    time.sleep(1)

for i in range(1,3):
    os.system('cls')
    print(i*' ' + 'gratulacje')
    time.sleep(1)

for i in range(1,3):
    os.system('cls')
    print(i*' ' + '恭喜')
    time.sleep(1)

for i in range(1,3):
    os.system('cls')
    print(i*' ' + 'Congratulazioni')
    time.sleep(1)

for i in range(1,3):
    os.system('cls')
    print(i*' ' + 'Котлыйбыз')
    time.sleep(1)

for i in range(1,3):
    os.system('cls')
    print(i*' ' + 'تهانينا')
    time.sleep(1)

for i in range(1,3):
    os.system('cls')
    print(i*' ' + 'Gratulujeme')

import turtle
import random

skk = turtle.Turtle()
lista=['red','blue']
for i in range(40):
    skk.color(random.choice(lista))
    skk.forward(70)
    skk.right(90)
    skk.color(random.choice(lista))
    skk.forward(40)
    skk.right(100)
