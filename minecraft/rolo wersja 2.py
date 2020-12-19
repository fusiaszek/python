from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
xg= gracz.x
yg= gracz.y
zg = gracz.z
rozmiar=5
ygora=rozmiar
for y in range(rozmiar):
    for z in range(rozmiar):
        for x in range(rozmiar):
                if x==0 or z==0 or z==rozmiar-1 or x==rozmiar-1 or y==0 or y==rozmiar-1:
                    mc.setBlock(xg + x, yg + y, zg + z, 213)
rozmiar=rozmiar+2
dach=int((rozmiar+1)/2)
for y in range(dach):
    for z in range(rozmiar):
        for x in range(rozmiar):
            mc.setBlock(xg+y+x-1,yg+ygora+y,zg+y+z-1,213)
    rozmiar=rozmiar-2