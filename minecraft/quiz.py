# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i)
#     if i==5:
#         break
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
u=[4,4,8,4,9,1,2]
for i in u:
    if u[0]==u[i]:
        elementy=True
        mc.setBlock(xg,yg,zg,210)
    else:
        elementy=False
        mc.setBlock(xg,yg,zg,211)
        break
print(elementy)