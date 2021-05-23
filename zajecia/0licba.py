x=0
z=0
y=0
while y!='x':
    y=input('wcisnij + lub - lub * lub / (jesli chces wyjsc do wcisnij x) ')
    if y=='x':
        exit(0)
    x=int((input('podaj liczbe ')))
    z=int((input('podaj liczbe ')))
    if y=='+':
        print(x+z)
    if y=='-':
        print(x-z)
    if y=='*':
        print(x*z)
    if y=='/' and z!=0:
        print(x/z)
    if y=='/' and z==0:
        print('nie mozna dzielic przez 0')
    if y!='+' and y!='-' and y!='*' and y!='/':
        print('nie ma takiej funkcji jak '+str(y))