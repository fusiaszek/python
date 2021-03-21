from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# def sloneczko(rozmiar):
# gracz = mc.player.getTilePos()
# zg = gracz.z
# xg = gracz.x
#     przesun=int(rozmiar/2)
#     for z in range(rozmiar):
#          for x in range(rozmiar):
#             mc.setBlock(xg+x-przesun,yg+5,zg+z-przesun,41)
# gracz = mc.player.getTilePos()
# yg=gracz.y
# sloneczko(2)
# yg = gracz.y+1
# sloneczko(4)
# gracz = mc.player.getTilePos()
# yg = gracz.y+2
# sloneczko(6)
# yg=gracz.y+3
# sloneczko(8)
# yg=gracz.y+4
# sloneczko(6)
# yg=gracz.y+5
# sloneczko(4)
# yg=gracz.y+6
# sloneczko(2)
#
# def wiartaczek(rozmiar):
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
#     for y in range(rozmiar+2):
#         mc.setBlock(xg,yg+y,zg,191)
#     for tin in range(rozmiar):
#         mc.setBlock(xg+tin,yg+rozmiar,zg+tin,151)
#     # for t in range(rozmiar):
#     #     mc.setBlock(xg-t,yg+rozmiar,zg-t,151)
# wiartaczek(3)

# def przestrzen(rozmiar):
#     for y in range(rozmiar):
#         for x in range(rozmiar):
#             for z in range(rozmiar):
#                 mc.setBlock(xg+x,yg+y,zg+z,0)
# przestrzen(30)