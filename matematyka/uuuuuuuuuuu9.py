from random import randrange
for trr in range(100):
    x=randrange(1,10)
    y=randrange(1,10)
    if trr<=50:
        w=int(input(str(x)+str('+')+str(y)+str(' podaj sume ')))
        i=x+y
    if trr>50:
        w=int(input(str(x)+str('*')+str(y)+str(' podaj iloczyn ')))
        i=x*y
    if w==i:
        print('dobrze')
    if w!=i:
        print('zle')
        exit(trr)
# from random import randrange
# for x in range(3):
#     print(str('M ')+str(randrange(1,101))+str('/')+str(randrange(1,101)))
# print(' ')
# for y in range(3):
#     print(str('A ')+str(randrange(1,101))+str('/')+str(randrange(1,101)))
