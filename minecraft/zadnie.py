from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
u=[2,9,6,2,1,6]
o=0
for i in u:
    if i%2==0:
        o+=i
y=o*u[5]
for l in range(y+1):
    mc.setBlock(xg,yg+l,zg,5)
    if l%10==0 and l!=0:
        mc.setBlock(xg,yg+l,zg,1)