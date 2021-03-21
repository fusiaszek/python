# x=str(input('podaj nazwe miasta w ktorym mieszkasz '))
# i=str(input('podaj nazwe ulicy przy ktorej mieszkasz '))
# def miasto_i_ulica(miasto,ulica):
#     print('mieszkasz w '+miasto+' na ulicy '+ulica)
# miasto_i_ulica(x,i)

# from random import randrange
# from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
gracz = mc.player.getTilePos()
zg = gracz.z
xg = gracz.x
yg = gracz.y
pxg = gracz.x
pzg = gracz.z
pyg = gracz.y
# def losowe_miejsce(x,z):
#     mc.player.setTilePos(x,100,z)
# losowe_miejsce(randrange(-111,6897),randrange(-171,6997))

def posadz_drzewo():
    dach=yg
    for t in range(3):
        mc.setBlock(xg+1,yg+t,zg+1,89)
        dach=dach+1
    rozmiar=3
    rozmiar=rozmiar+2
    dach=int((rozmiar+1)/2)
    for y in range(dach):
        for z in range(rozmiar):
            for x in range(rozmiar):
                mc.setBlock(pxg+y+x-1,pyg+y+dach,pzg+y+z-1,41)
        rozmiar=rozmiar-2
posadz_drzewo()