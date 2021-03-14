def usun_wszystko_przed(lista, liczba):
    u=[]
    for i in lista:
        if i>=liczba:
            u.append(i)
    print(u)
usun_wszystko_przed([7, 9, 2, 3, 1, 4], 5)