from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
xp=0
zp=0
xc = randrange(100, 150)
zc = randrange(100, 150)
mc.setBlock(xc, 100, zc, 198)
while True:
    gracz = mc.player.getTilePos()
    xg = gracz.x
    zg = gracz.z
    yg = gracz.y
    if abs(xc-xg)<abs(xc-xp) or abs(zc-zg)<abs(zc-zp):
        print('cieplo')
    if abs(xc-xg)>abs(xc-xp) or abs(zc-zg)>abs(zc-zp):
        print('zimniej')
    if xg==xc and zg==zc and yg==101:
        print('znalazles')
    xp=xg
    zp=zg
