import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
e3=int(input('do ilu czhcesz losowac? '))
losowaliczba=random.randint(1,e3)
x=int(input('podaj liczbe od 1 do '+str(e3 )))
if x==losowaliczba:
    print('zgadles')
else:
    mc.postToChat('niezgadles!!!'+str(losowaliczba ))

