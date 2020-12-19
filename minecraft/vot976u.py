from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
xg = gracz.x
yg = gracz.y
zg = gracz.z
lista=['KAROL','HENRYK','BARTEK']
x=1
while x!=0:
    x=int(input('podaj 0 lub 1 lub 2 lub 3 '))
    if x==1:
        caat=int(input('podaj numer bloczka'))
        mc.setBlock(xg,yg,zg+5, caat)
    if x == 2:
        for ff in range(100):
            mc.setBlock(xg,yg-ff,zg,0)
    if x==3:
        mc.player.setTilePos(randrange(54,254),100,randrange(412,601))
    if x==4:
        for bla_bla in range(4):
            mc.setBlock(xg,yg+bla_bla,zg,213)
    if x==5:
        mc.player.setTilePos(100,100,100)
    if x==6:
        mc.player.setTilePos(810, 65, 586)
    if x==7:
        mc.player.setTilePos(183, 81, 1267)
    if x==8:
        mc.player.setTilePos(207,54,1252)
