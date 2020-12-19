from mcpi.minecraft import Minecraft

mc = Minecraft.create()

gracz = mc.player.getTilePos()

x = gracz.x
y = gracz.y
z = gracz.z
Q=input('czy chcesz zbudować maly schody?')

if Q == '1':
    for a in range(2):
        x+=a;
        y+=a;
        mc.setBlock(x,y,z,100)
        mc.setBlock(x+1,y+1,z,100)
        mc.setBlock(x+2, y+2, z, 100)
        mc.setBlock(x+3,y+3, z, 100)
