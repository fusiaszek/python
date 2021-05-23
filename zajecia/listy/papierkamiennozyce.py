import random
a=random.randint(0,2)
wynik1=0
wynik2=0
wygrana=''
while wynik2!=3 and wynik1!=3:
    d = str(input('podaj kamien,papier lub nozyce:'))
    print(d)
    print(a)
    if a==0:
        aopis='kamien'
    if a==1:
        aopis='papier'
    if a==2:
        aopis='nozyce'
    if aopis=='kamien' and d=='papier':
        wynik1+=1
        wygrana='gracz'
    if aopis=='kamien' and d=='nozyce':
        wygrana='komputer'
    if aopis=='kamien' and d=='kamien':
        wygrana='remis'
    if aopis=='papier' and d=='papier':
        wynik1+=1
        wygrana='remis'
    if aopis=='papier' and d=='nozyce':
        wygrana='gracz'
    if aopis=='papier' and d=='kamien':
        wygrana='komputer'
    if aopis=='nozyce' and d=='papier':
        wynik1+=1
        wygrana='komputer'
    if aopis=='nozyce' and d=='nozyce':
        wygrana='remis'
    if aopis=='nozyce' and d=='kamien':
        wygrana='gracz'
    print('komputer wylosowal '+str(aopis))
    # print(str(wynik1)+str('-')+str(wynik2))
    print(wygrana)