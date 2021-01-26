from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
rozmiar=5
def podloga():
    global x, z
    for x in range(rozmiar):
        for z in range(rozmiar):
            mc.setBlock(xg + x, yg, zg + z, 100)
podloga()
wysokosc = rozmiar * 2
for y in range(wysokosc):
    for x in range(rozmiar):
        mc.setBlock(xg + x, yg + y, zg, 100)
        if x==int(rozmiar/2) and y%2!=0:
            mc.setBlock(xg+x,yg+y,zg,50)
        if x%2==0:
            mc.setBlock(xg + x, yg + wysokosc, zg, 100)
for y in range(wysokosc):
    for z in range(rozmiar):
        mc.setBlock(xg,yg+y,zg+z,100)
        if z%2==0:
            mc.setBlock(xg, yg + wysokosc, zg + z, 100)
for y in range(wysokosc):
    for x in range(rozmiar):
        mc.setBlock(xg+x,yg+y,zg+rozmiar-1,100)
        if x%2==0:
            mc.setBlock(xg + x, yg + wysokosc, zg + rozmiar-1, 100)
for y in range(wysokosc):
    for z in range(rozmiar):
        mc.setBlock(xg+rozmiar-1,yg+y,zg+z,100)
        if z%2==0:
            mc.setBlock(xg + rozmiar-1, yg + wysokosc, zg + z, 100)