from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    gracz = mc.player.getTilePos()
    zg = gracz.z
    xg = gracz.x
    yg = gracz.y
    if mc.getBlock(xg,yg-1,zg)==9:
        mc.setBlock(xg,yg-1,zg,79)


