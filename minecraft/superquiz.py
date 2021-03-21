from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
u=[4,4,8,4]
for i in u:
    if u[0]==u[i]:
        elementy=True
    else:
        elementy=False
        break
print(elementy)