from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    gracz = mc.player.getTilePos()
    xg = gracz.x
    yg = gracz.y
    zg = gracz.z
    if zg>6528 and zg<6536 and xg<5320 and xg>5315:
        print('jestem w domu')
    if zg>6537 and zg<6539:
        print('jestem w ogodku')



