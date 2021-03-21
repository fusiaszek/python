from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
def przestrzen(rozmiar):
    for y in range(rozmiar):
        for x in range(rozmiar):
            for z in range(rozmiar):
                mc.setBlock(xg+x,yg+y,zg+z,0)
przestrzen(50)
