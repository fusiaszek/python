from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
pxg = gracz.x
pzg = gracz.z
pyg = gracz.y
while True:
    gracz = mc.player.getTilePos()
    xg = gracz.x
    zg = gracz.z
    yg = gracz.y
    rozmiar=11
    rozmiar=rozmiar+2
    dach=int((rozmiar+1)/2)
    for y in range(dach):
        for z in range(rozmiar):
            for x in range(rozmiar):
                mc.setBlock(pxg+y+x-1,pyg+y,pzg+y+z-1,213)
        rozmiar=rozmiar-2
        if zg==pzg+5 and xg==pxg+5 and yg==pyg+7:
            print('jestes na sczycie')