from random import randrange
rozmiar=7
lista=[0]*rozmiar
for x in range(rozmiar):
    lista[x]=randrange(10,20)
print(lista)
lista.append(4)
lista.append(4)
lista.append(4)
lista.append(4)
lista.append(4)
lista.append('Pa Pa 4 witaj 7')
lista.append(7)
lista.append(7)
lista.append(7)
print(lista)