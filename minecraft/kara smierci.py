from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    gracz = mc.player.getTilePos()
    zg = gracz.z
    xg = gracz.x
    yg = gracz.y
    if mc.getBlock(xg,yg-1,zg+2)==8 or mc.getBlock(xg,yg-1,zg+2)==9 or mc.getBlock(xg+2,yg-1,zg)==8 or mc.getBlock(xg+2,yg-1,zg)==9:
        mc.setBlock(xg,yg-1,zg,79)
        mc.setBlock(xg+1,yg-1,zg,79)
        mc.setBlock(xg-1,yg-1,zg,79)
        mc.setBlock(xg,yg-1,zg-1,79)
        mc.setBlock(xg,yg-1,zg+1,79)
        mc.setBlock(xg+2,yg-1,zg,79)
        mc.setBlock(xg-2,yg-1,zg,79)
        mc.setBlock(xg,yg-1,zg-2,79)
        mc.setBlock(xg,yg-1,zg+2,79)
        mc.setBlock(xg+1,yg-1,zg+1,79)
        mc.setBlock(xg-1,yg-1,zg-1,79)
        mc.setBlock(xg+1,yg-1,zg-1,79)
        mc.setBlock(xg-1,yg-1,zg+1,79)
