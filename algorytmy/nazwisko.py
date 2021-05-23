# x=''
# list=[]
# dlugosci=[]
# najdluzsze=0
# najkrotsze=0
# costam=0
# while x!='x' and x!='X':
#     x=str(input('podaj imie'))
#     if x!='x' and x!='X':
#         list.append(x)
# for i in list:
#     dlugosci.append(len(i))
# for y in dlugosci:
#     if y>najdluzsze:
#         najdluzsze=y
# for a in dlugosci:
#     if y>najkrotsze:
#         najkrotsze=y
# for t in dlugosci:
#     costam+=t
# liczbawyrazow=len(list)
# print('najdluzszy wyraz ma '+str(najdluzsze)+str(' liter'))
# print('najkrutszy wyraz ma '+str(najkrotsze)+str(' liter'))
# print('srednia liczba liter to '+str(costam/liczbawyrazow))
import turtle
import random

skk = turtle.Turtle()
lista=['red','blue']
for i in range(40):
    skk.color(random.choice(lista))
    skk.forward(70)
    skk.right(90)
    skk.color(random.choice(lista))
    skk.forward(40)
    skk.right(100)

turtle.done()