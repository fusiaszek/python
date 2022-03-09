slowo1 = input('Podaj 1 slowo\n')
slowo2 = input('Podaj 2 slowo\n')
dlugosc = len(slowo1)+1
szerokosc = len(slowo2)+1
def nozyczki(slowo, dlugosc):
    slowo_zwrotne = ''
    for i in range(dlugosc):
        slowo_zwrotne += slowo[i]
    return slowo_zwrotne
def ostatnia(slowo):
    return slowo[len(slowo)-1]
def najwieksza(liczba1, liczba2):
    wieksza = liczba1
    if liczba2 > liczba1:
        wieksza = liczba2
    return wieksza
tablica = [([(0)for i in range(dlugosc)])for j in range(szerokosc)]
for x in range(1, szerokosc):
    for y in range(1, dlugosc):
        dodaj = 0
        if ostatnia(nozyczki(slowo1, y)) == ostatnia(nozyczki(slowo2, x)):
            dodaj = 1 
        tablica[x][y] = najwieksza(tablica[x-1][y], tablica[x][y-1]) + dodaj
print(tablica[szerokosc-1][dlugosc-1])