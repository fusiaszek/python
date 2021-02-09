from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
rozmiar=11
for poziom in range(int(rozmiar/2+1)):
    rozmiar_poziom = rozmiar - 2 * poziom
    przesun=int(rozmiar_poziom/2)
    for z in range(rozmiar_poziom):
        for x in range(rozmiar_poziom):
            mc.setBlock(xg+x-przesun,yg+poziom,zg+z-przesun,1)
for y in range(rozmiar):
    mc.setBlock(xg+int(rozmiar/2),yg-y,zg+int(rozmiar/2),1)
    mc.setBlock(xg-int(rozmiar/2),yg-y,zg-int(rozmiar/2),1)
    mc.setBlock(xg+int(rozmiar/2),yg-y,zg-int(rozmiar/2),1)
    mc.setBlock(xg-int(rozmiar/2),yg-y,zg+int(rozmiar/2),1)
for z in range(rozmiar):
    for x in range(rozmiar):
        mc.setBlock(xg+x-int(rozmiar/2),yg-rozmiar,zg+z-int(rozmiar/2),1)
