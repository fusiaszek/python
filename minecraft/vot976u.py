import math
from random import randrange
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# gracz = mc.player.getTilePos()
# xg = gracz.x
# zg = gracz.z
# yg = gracz.y
# lista=['KAROL','HENRYK','BARTEK']
# x=1
# while x!=0:
#     x=int(input('podaj 0 lub 1 lub 2 lub 3 '))
#     if x==1:
#         caat=int(input('podaj numer bloczka'))
#         mc.setBlock(xg,yg,zg+5, caat)
#     if x == 2:
#         for ff in range(100):
#             mc.setBlock(xg,yg-ff,zg,0)
#     if x==3:
#         mc.player.setTilePos(randrange(54,254),100,randrange(412,601))
#     if x==4:
#         for bla_bla in range(4):
#             mc.setBlock(xg,yg+bla_bla,zg,213)
#     if x==5:
#         mc.player.setTilePos(100,100,100)
#     if x==6:
#         mc.player.setTilePos(810, 65, 586)
#     if x==7:
#         mc.player.setTilePos(183, 81, 1267)
#     if x==8:
#         mc.player.setTilePos(207,54,1252)

# while True:
#     gracz = mc.player.getTilePos()
#     xg = gracz.x
#     yg = gracz.y
#     zg = gracz.z
#     mc.setBlock(xg,yg-1,zg,213)

# b=randrange(100,154)
# v=randrange(100,150)
# mc.setBlock(v,160,b,213)
# while True:
#     gracz = mc.player.getTilePos()
#     xg = gracz.x
#     yg = gracz.y
#     zg = gracz.z
#     mc.postToChat(xg)
#     mc.postToChat(yg)
#     mc.postToChat(zg)
#     mc.postToChat('')
#     mc.postToChat(b)
#     mc.postToChat(v)
#     if xg==v and zg==b:
#         mc.postToChat('znalazlez')
#     distance = math.sqrt((xg - v) ** 2 + (zg - b) ** 2)
#     print(distance)

# gracz = mc.player.getTilePos()
# xg = gracz.x
# zg = gracz.z
# yg = gracz.y
# wysokosc=yg+10
# while True:
#     rozmiar = 3
#     for x in range(rozmiar):
#         for z in range(rozmiar):
#             aktualnyygracza = mc.player.getTilePos().y
#             aktualnyzgracza = mc.player.getTilePos().z
#             aktualnyxgracza = mc.player.getTilePos().x
#             if aktualnyygracza==wysokosc+1 and aktualnyxgracza>=xg and aktualnyxgracza<=xg+rozmiar-1 and aktualnyzgracza>=zg and aktualnyzgracza<=zg+rozmiar-1:
#                 blok1 = 213
#             else:
#                 blok1 = 1
#             if aktualnyygracza==wysokosc+1 and aktualnyxgracza-6>=xg and aktualnyxgracza-6<=xg+rozmiar-1 and aktualnyzgracza>=zg and aktualnyzgracza<=zg+rozmiar-1:
#                 blok2 = 213
#             else:
#                 blok2 = 1
#             if aktualnyygracza==wysokosc+1 and aktualnyxgracza>=xg+6 and aktualnyxgracza<=xg+6+rozmiar-1 and aktualnyzgracza>=zg+6 and aktualnyzgracza<=zg+6+rozmiar-1:
#                 blok3 = 213
#             else:
#                 blok3 = 1
#             mc.setBlock(xg + x, wysokosc, zg + z, blok1)
#             mc.setBlock(xg + 6 + x, wysokosc, zg + z, blok2)
#             mc.setBlock(xg + 6 + x, wysokosc, zg + 6 + z, blok3)

# gracz = mc.player.getTilePos()
# xg = gracz.x
# zg = gracz.z
# yg = gracz.y
# wysokosc=yg+10
# while True:
#     rozmiar = 3
#     for x in range(rozmiar):
#         for z in range(rozmiar):
#             aktualnyygracza = mc.player.getTilePos().y
#             aktualnyzgracza = mc.player.getTilePos().z
#             aktualnyxgracza = mc.player.getTilePos().x
#             if aktualnyygracza==wysokosc+1 and aktualnyxgracza>=xg and aktualnyxgracza<=xg+rozmiar-1 and aktualnyzgracza>=zg and aktualnyzgracza<=zg+rozmiar-1:
#                 blok1 = 213
#             else:
#                 blok1 = 1
#             if aktualnyygracza==wysokosc+1 and aktualnyxgracza-6>=xg and aktualnyxgracza-6<=xg+rozmiar-1 and aktualnyzgracza>=zg and aktualnyzgracza<=zg+rozmiar-1:
#                 blok2 = 213
#             else:
#                 blok2 = 1
#             if aktualnyygracza==wysokosc+1 and aktualnyxgracza>=xg+6 and aktualnyxgracza<=xg+6+rozmiar-1 and aktualnyzgracza>=zg+6 and aktualnyzgracza<=zg+6+rozmiar-1:
#                 blok3 = 213
#             else:
#                 blok3 = 1
#             mc.setBlock(xg + x, wysokosc, zg + z, blok1)
#             mc.setBlock(xg + 6 + x, wysokosc, zg + z, blok2)
#             mc.setBlock(xg + 6 + x, wysokosc, zg + 6 + z, blok3)

# gracz = mc.player.getTilePos()
# pxg = gracz.x
# pzg = gracz.z
# pyg = gracz.y
# while True:
#     gracz = mc.player.getTilePos()
#     xg = gracz.x
#     zg = gracz.z
#     yg = gracz.y
#     rozmiar=11
#     rozmiar=rozmiar+2
#     dach=int((rozmiar+1)/2)
#     for y in range(dach):
#         for z in range(rozmiar):
#             for x in range(rozmiar):
#                 mc.setBlock(pxg+y+x-1,pyg+y,pzg+y+z-1,213)
#         rozmiar=rozmiar-2
#         if zg==pzg+5 and xg==pxg+5 and yg==pyg+7:
#             print('jestes na sczycie')