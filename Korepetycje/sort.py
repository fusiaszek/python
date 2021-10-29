print('Pomysł 1')
import random
lista = [20,8,-3,-10,56,72,19,-1]
print(sorted(lista))

print('Pomysł 2')
def sortowanie(lista):
    lista = lista
    lista_posortowana = []
    for j in range(len(lista)):
        a = lista[0]
        for i in lista:
            if i<a:
                a=i
        lista.remove(a)
        lista_posortowana.append(a)       
    return lista_posortowana
print(sortowanie([20,8,-3,-10,56,72,19,-1]))