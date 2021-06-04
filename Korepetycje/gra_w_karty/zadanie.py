import random

# lista = [1,2,3,4]
# lista_zagniezdzona = [
#     lista,
#     lista, 
#     lista,
#     lista
# ]
# lista_zagniezdzona2 = [["puste" for i in range(4)] for j in range(4)]
# for lista in lista_zagniezdzona2:
#     print(*lista)
random.seed(53)

alfabet = "ABCDEFGHIJKLMNOPRSTUWYZ"

def losuj_literke():
    rand_index = random.randint(0, len(alfabet)-1)
    wylosowana_literka = alfabet[rand_index]
    return wylosowana_literka

def inicjalizacja_board(board):
    pass

def drukuj_board(board):
    for wiersz in board:
        print(*wiersz)

def generate_board(height, width):
    board = [["-" for i in range(1, width+1)] for i in range(1, height+1)]
    ilosc_par = (height * width) / 2
    rodzaje_kart = []
    wylosowana_literka = "A"

    for i in range(int(ilosc_par)):
        while(wylosowana_literka in rodzaje_kart):
            wylosowana_literka = losuj_literke()
        rodzaje_kart.append(wylosowana_literka)
    
    print(rodzaje_kart)


generate_board(4, 4)

