from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def slup(block,ilosc):
    for t in range(ilosc):
        mc.setBlock(randrange(5323,5425),121,randrange(6656,6745),block)
slup(201,2)