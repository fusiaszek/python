from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
for y in range(3):
    plik=open('labirynt.csv','r')
    for x in range(16):
        linia=plik.readline()
        zerolubjeden=linia.split(',')
        for z in range(16):
                mc.setBlock(xg+x,yg+y,zg+z,int(zerolubjeden[z]))