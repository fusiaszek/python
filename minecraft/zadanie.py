from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
xg= gracz.x
yg= gracz.y
zg = gracz.z
x=-1
while x!=0:
    x = int(input('podaj licbe '))
    if x==1:
        rozmiar = 5
        dach = int((rozmiar + 1) / 2)
        for y in range(dach):
            for z in range(rozmiar):
                for x in range(rozmiar):
                    mc.setBlock(xg + y + x - 1, yg + y, zg + y + z - 1, 213)
            rozmiar = rozmiar - 2
    if x==4:
        for ii in range(3):
             mc.setBlock(xg+ii,yg+ii,zg,213)
    if x==2:
        for ttk in range(5):
           mc.setBlock(xg+ttk,yg-ttk,zg,0)
