import random

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
    for wiersz in board:
        print(wiersz)

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
     
height = 4
width = 4
board = generate_board(height, width)
karty = losuj_karty(height, width)
uzupelnij_board(height, width, board, karty)
drukuj_board(board)
