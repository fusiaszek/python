from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
for i in range(10):
    mc.setBlock(zg,yg-1,zg,i)
    mc.player.setTilePos(xg+1,yg,zg)