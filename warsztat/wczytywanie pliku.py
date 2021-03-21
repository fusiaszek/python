dane=open('dane.txt','r')
for linia in dane:
    linia=linia.replace('\n', '')
    lista=linia.split(' ')
    print('Liczba {0} podniesiona do potegi {1} daje wynik {2}'.format(lista[0],lista[1],int(int(lista[0])**float(lista[1]))))