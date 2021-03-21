
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
pxg = gracz.x
pzg = gracz.z
pyg = gracz.y
# def posadz_drzewo():
#     dach=yg
#     for t in range(3):
#         mc.setBlock(xg+1,yg+t,zg+1,89)
#         dach=dach+1
#     rozmiar=3
#     rozmiar=rozmiar+2
#     dach=int((rozmiar+1)/2)
#     for y in range(dach):
#         for z in range(rozmiar):
#             for x in range(rozmiar):
#                 mc.setBlock(pxg+y+x-1,pyg+y+dach,pzg+y+z-1,41)
#         rozmiar=rozmiar-2
# posadz_drzewo()

from random import randrange
def slup(block,ilosc):
    for t in range(ilosc):
        mc.setBlock(randrange(5323,5425),121,randrange(6656,6745),block)
slup(201,2)