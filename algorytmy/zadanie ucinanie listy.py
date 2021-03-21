def usun_wszystko_przed(lista, liczba):
    u=[]
    for i in lista:
        if i>=liczba:
            u.append(i)
    print(u)
usun_wszystko_przed([1,2,3,4,5,6], 5)