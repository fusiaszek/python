def halo(lista,liczba):
    u=[]
    for i in lista:
        if i>=liczba:
            u.append(i)
    print(u)
halo([7,9,2,3,1,4],5)