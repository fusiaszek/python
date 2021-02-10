from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    gracz = mc.player.getTilePos()
    zg = gracz.z
    xg = gracz.x
    yg = gracz.y
    if xg<5420 and xg>5415 and zg>6505 and zg<6512:
        print('jestes w ogrodku')
    else:
        print('nie jestes w ogrodku')
