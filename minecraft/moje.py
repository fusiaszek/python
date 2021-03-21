from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
xg = gracz.x
yg = gracz.y
zg = gracz.z
#blok 90 to portal do netheru
while True:
    if mc.getBlock(xg,yg-1,zg)==0:
        mc.setBlock(xg,yg-1,zg,14)
    # if mc.getBlock(xg+1,yg-1,zg)==14 and mc.getBlock(xg-1,yg-1,zg)==14:
    #     mc.setBlock(xg+1,yg-1,zg,0)
    #     mc.setBlock(xg-1,yg-1,zg,0)