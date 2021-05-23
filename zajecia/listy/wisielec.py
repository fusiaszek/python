import turtle
a=0
don = turtle.Turtle()
print('''Czas zagrac w wisielca
Zacznij zgadywac''')
password='chmura'
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
        a+=1
    if a==1:
        don.goto(100,0)
        don.goto(50,0)
    if a==2:
        don.goto(50,150)
    if a==3:
        don.goto(150,150)
    if a==4:
        don.goto(150,110)
    if a==5:
        don.fillcolor('black')
        don.begin_fill()
        don.circle(10)
        don.end_fill()
    if a==6:
        don.goto(150,70)
    if a==7:
        don.goto(120,40)
        don.goto(150,70)
    if a==8:
        don.goto(180,40)
        don.goto(150,70)
        don.goto(150,100)
    if a==9:
        don.goto(110,80)
        don.goto(150,100)
    if a==10:
        don.goto(190,80)
    if liczbazyc==0:
        print('przegrales')
        print('haslo to '+str(password))
        input('nacisnij enter aby zakonczyc')