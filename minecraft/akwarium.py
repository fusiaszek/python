from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
xg = gracz.x
yg = gracz.y
zg = gracz.z
def akwarium():
    for y in range(4):
        for x in range(5):
            mc.setBlock(xg+x,yg+y,zg,160)
    for y in range(4):
        for x in range(5):
            mc.setBlock(xg+x,yg+y,zg+5,160)
    for y in range(4):
        for z in range(6):
            mc.setBlock(xg,yg+y,zg+z,160)
    for y in range(4):
        for z in range(6):
            mc.setBlock(xg+5,yg+y,zg+z,160)
    for y in range(4):
        for x in range(5):
            mc.setBlock(xg+x,yg+y,zg,160)
    for y in range(4):
        for x in range(4):
            for z in range(4):
                mc.setBlock(xg+x+1,yg+y,zg+z+1,8)
    for x in range(6):
        for z in range(6):
            mc.setBlock(xg+x,yg,zg+z,95)
akwarium()
