from random import randrange
rozmiar=10
suma=0
najwieksza_liczba=0
najmniejsza_liczba=rozmiar
lista=[0]*rozmiar
for i in range(rozmiar):
    lista[i]=randrange(1,rozmiar)
for x in range(rozmiar):
    suma=suma+lista[x]
for G in range(rozmiar):
    if lista[G]>najwieksza_liczba:
        najwieksza_liczba=lista[G]
for M in range(rozmiar):
    if lista[M]<najmniejsza_liczba:
        najmniejsza_liczba=lista[M]
print('wylosowana lista to '+str(lista))
print('suma wszystkich liczb z listy wynosi ' + str(suma))
print('najwieksza liczba to '+str(najwieksza_liczba))
print('najmniejsza liczba to '+str(najmniejsza_liczba))
print('srednia to '+str(suma/rozmiar))
