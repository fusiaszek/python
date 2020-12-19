from random import randrange
lista=[0]*10
for G in range(10):
    lista[G]=randrange(1,10)
print(lista)
lista.append(randrange(100,1000))
lista[randrange(1,10)]=randrange(50,100)
print(lista)
for X in lista:
    if X%2==0:
        print(X)
