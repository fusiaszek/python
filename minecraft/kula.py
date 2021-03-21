from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
rozmiar=10
def sloneczko(rozmiar):
        przesun=int(rozmiar/2)
        for z in range(rozmiar):
             for x in range(rozmiar):
                mc.setBlock(xg+x-przesun,yg+5,zg+z-przesun,213)
gracz = mc.player.getTilePos()
yg=gracz.y
sloneczko(2)
yg = gracz.y+1
sloneczko(4)
gracz = mc.player.getTilePos()
yg = gracz.y+2
sloneczko(6)
yg=gracz.y+3
sloneczko(8)
yg=gracz.y+4
sloneczko(6)
yg=gracz.y+5
sloneczko(4)
yg=gracz.y+6
sloneczko(2)
