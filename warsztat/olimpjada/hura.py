n = int(input())
wiwat = 'Wiwat!'
hurra = 'Hurra!'
zupa = 'Super!'
for i in range(1, n+1):
    a = i % 7 == 0
    b = i % 11 == 0
    if not a and not b:
        print(i)
    elif a and b:
        print(wiwat)
    elif a:
        print(hurra)
    elif b:
        print(zupa)
