from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
xg= gracz.x
yg= gracz.y
zg = gracz.z
rozmiar=7
ygora=rozmiar
for i in range(rozmiar):
    for t in range(rozmiar):
        for o in range(rozmiar):
                mc.setBlock(xg+o+1,yg+t,zg+i+1,213)
rozmiar=rozmiar+2
dach=int((rozmiar+1)/2)
for y in range(dach):
    for z in range(rozmiar):
        for x in range(rozmiar):
            mc.setBlock(xg+y+x,yg+ygora+y,zg+y+z,213)
    rozmiar=rozmiar-2