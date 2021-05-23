print('''Czas zagrac w wisielca
Zacznij zgadywac''')
password='gasnica'
liczbazyc=10
zgadywanehaslo=''
while liczbazyc>0:
    niezgadniete=0
    for char in password:
        if char in zgadywanehaslo:
            print(char)
        else:
            print('_')
            niezgadniete+=1
    if niezgadniete==0:
        print('wygrales')
        exit(0)
    literka=input('podaj literke: ')
    zgadywanehaslo+=literka
    if literka not in password:
        liczbazyc-=1
        print('zle')
        print('pzostalo ci '+str(liczbazyc)+str(' zyc'))
    if liczbazyc==0:
        print('przegrales')
