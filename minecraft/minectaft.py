from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
x = gracz.x
y = gracz.y
z = gracz.z
# lista=[0]*10
# for x2 in range(10):
#     lista[x2]=randrange(10)
#     mc.postToChat(lista[x2])
# lista.append(randrange(8,13))
# mc.postToChat(lista)
# for Jj in range(10):
#     mc.setBlock(x,y,z+Jj, lista[x2]+18)
print(x)
print(y)
print(z)