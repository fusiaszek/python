import time
from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
time.sleep(10)
punkty=0
uderzenia=mc.events.pollBlockHits()
for i in uderzenia:
    x = i.pos.x
    y = i.pos.y
    z = i.pos.z
    punkty+=mc.getBlock(x,y,z)
    print(str(punkty))
mc.postToChat(str(punkty))