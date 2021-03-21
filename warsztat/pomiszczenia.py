dane = open('dane.txt', 'r')
rozmiar = int(dane.readline())
tablica = [[' ' for i in range(rozmiar)] for i in range(rozmiar)]
wynik = 0
wiersz = 0
kolumna = 0
for linia in dane:
    linia = linia.replace("\n", '')
    for znak in linia:
        tablica[kolumna][wiersz] = znak
        kolumna += 1
    wiersz += 1
    kolumna = 0
print(wynik)
print(tablica[2][3])  # pusty znak
print(tablica[2][2])  # * gwiazdka
