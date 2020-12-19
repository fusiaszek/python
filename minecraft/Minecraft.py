# from random import randrange
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# gracz = mc.player.getTilePos()
# x = gracz.x
# y = gracz.y
# z = gracz.z
# lista=[0]*10
# O=11000
# for xty in range(10):
#     lista[xty]=randrange(900,1100)
# for yrr in lista:
#     if O>yrr:
#         O=yrr
# mc.player.setTilePos(O,100,100)
# print(lista)
# mc.postToChat(O)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
lista=[]
p=0
o=0
podanaliczba=input('podaj liczbe ')
o=o+int(podanaliczba)
lista.append(int(podanaliczba))
print(lista)
print('maksymalna liczba to ' + str(max(lista)))
print('minimalna liczba to ' + str(min(lista)))
while podanaliczba!='1':
    podanaliczba = input('podaj liczbe ')
    if podanaliczba!='':
        o=o+int(podanaliczba)
        lista.append(int(podanaliczba))
        mc.postToChat(lista)
        mc.postToChat('maksymalna liczba to '+str(max(lista)))
        mc.postToChat('minimalna liczba to '+str(min(lista)))
        mc.postToChat('suma to ' + str(o))

