from mcpi.minecraft import Minecraft
mc = Minecraft.create()

gracz = mc.player.getTilePos()
xg = gracz.x
zg = gracz.z
yg = gracz.y
wysokosc=yg+10
blok1 = 1
blok2 = 1
blok3 = 1
while True:
    rozmiar = 3
    for x in range(rozmiar):
        for z in range(rozmiar):
            aktualnyygracza = mc.player.getTilePos().y
            aktualnyzgracza = mc.player.getTilePos().z
            aktualnyxgracza = mc.player.getTilePos().x
            if aktualnyygracza==wysokosc+1 and aktualnyxgracza>=xg and aktualnyxgracza<=xg+rozmiar-1 and aktualnyzgracza>=zg and aktualnyzgracza<=zg+rozmiar-1:
                blok1 = 213
            if aktualnyygracza==wysokosc+1 and aktualnyxgracza-6>=xg and aktualnyxgracza-6<=xg+rozmiar-1 and aktualnyzgracza>=zg and aktualnyzgracza<=zg+rozmiar-1:
                blok2 = 213
            if aktualnyygracza==wysokosc+1 and aktualnyxgracza>=xg+6 and aktualnyxgracza<=xg+6+rozmiar-1 and aktualnyzgracza>=zg+6 and aktualnyzgracza<=zg+6+rozmiar-1:
                blok3 = 213
            mc.setBlock(xg + x, wysokosc, zg + z, blok1)
            mc.setBlock(xg + 6 + x, wysokosc, zg + z, blok2)
            mc.setBlock(xg + 6 + x, wysokosc, zg + 6 + z, blok3)
            if blok1==213 and blok2==213 and blok3==213:
                mc.postToChat("Wygrałeś")
