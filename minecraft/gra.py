from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# for bloki in range(1):
a=randrange(-132,-130)
b=randrange(1179,1181)
mc.setBlock(a,154,b,198)
mc.postToChat(a)
mc.postToChat(b)
while True:
    gracz = mc.player.getTilePos()
    zg=gracz.z
    xg=gracz.x
    yg = gracz.y
    print(xg)
    print(zg)
