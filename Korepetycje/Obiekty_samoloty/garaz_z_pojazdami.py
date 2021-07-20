import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

# img = mpimg.imread('f_117.jpg')
# imgplot = plt.imshow(img)
# plt.show()

class Samolot:

    def __init__(self, model, marka, rozpietosc_skrzydel=10) -> None:
        print("Tworze sobie samolot")
        self.rozpietosc_skrzydel = rozpietosc_skrzydel
        self.model = model
        self.marka = marka
    
    def __str__(self) -> str:
        return f'Rozpietosc skrzydel {self.rozpietosc_skrzydel}\nMarka {self.marka}\nModel {self.model}'

class SamolotWojenny(Samolot):

    def __init__(self, model, marka, rozpietosc_skrzydel, ilosc_rakiet, czy_posiada_dziala) -> None:
        super().__init__(model, marka, rozpietosc_skrzydel=rozpietosc_skrzydel)
        self.ilosc_rakiet = ilosc_rakiet
        self.czy_posiada_dziala = czy_posiada_dziala

    def wystrzel_rakiety(self, ile_rakiet):
        print(f'Wystrzele {ile_rakiet} rakiet!')
        for i in range(ile_rakiet):
            if self.ilosc_rakiet > 0:
                self.ilosc_rakiet -= 1
                print("Aktualna ilosc rakiet to ", self.ilosc_rakiet)
                print("BUMMMMM")
            else:
                print("nie ma juz rakiet!")
        return ile_rakiet

    def otrzymaj_arsenal(self, arsenal):
        self.arsenal = arsenal
        self.ilosc_rakiet = arsenal['rakiety']

class SamolotWsparcia(Samolot):

        def __init__(self, model, marka, rozpietosc_skrzydel, arsenal) -> None:
            super().__init__(model, marka, rozpietosc_skrzydel=rozpietosc_skrzydel)
            self.arsenal = arsenal

        def przekaz_przedmioty(self, liste_przedmiotow: tuple):
            for przedmiot in liste_przedmiotow:
                if self.arsenal.get(przedmiot):
                    continue
                return {}
            return 
                

        def przekaz_przedmiot(self, przedmiot):
            ilosc_do_oddania = self.arsenal[przedmiot] 
            self.arsenal[przedmiot] = 0
            return ilosc_do_oddania

class Lotnisko:

    def __init__(self) -> None:
        self.hangar = []

    def dodaj_samolot(self, samolot):
        self.hangar.append(samolot)
    
    def usun_samolot(self, samolot):
        self.hangar.remove(samolot)
        
    def przesun_samolot(self, pozycja, nowa_pozycja):
        self.hangar[pozycja], self.hangar[nowa_pozycja] = self.hangar[nowa_pozycja], self.hangar[pozycja]

class Czolg:

    def __init__(self, max_punkty_zycia) -> None:
        self.punkty_zycia = max_punkty_zycia

    def otrzymaj_obrazenia(self, obrazenia):
        if self.punkty_zycia <= obrazenia:
            print("WAAAAH Czolg wybuchl!")
        else:
            self.punkty_zycia -= obrazenia
            print(f"Czolg dostal {obrazenia} obrazen! Pozostalo {self.punkty_zycia} pktow zycia!")

przykladowy_samolot = Samolot('f-117', 'odrzutowiec')
print(przykladowy_samolot.rozpietosc_skrzydel)
print(przykladowy_samolot)

przykladowy_samolot_wojenny = SamolotWojenny('f-117','odrzutowiec wojenny', 20, 100, True)
#print(przykladowy_samolot_wojenny)
przykladowy_arsenal = {
    'rakiety' : 100,
    'amunicja dzialka' : 10000,
    'bomby' : 50,
    'jedzenie' : 100
}
przykladowy_samolot_wsparcia = SamolotWsparcia('Wsparcie', 'Samolot', 50, przykladowy_arsenal)
print(przykladowy_samolot_wsparcia.arsenal)

przykladowy_czolg = Czolg(10)

#obrazenia_runda_1 = przykladowy_samolot_wojenny.wystrzel_rakiety(10)
#przykladowy_czolg.otrzymaj_obrazenia(obrazenia_runda_1)

class Pilot:
    def __init__(self, imie_i_nazwisko: str):
        imie_i_nazwisko = imie_i_nazwisko.split(' ')
        self.imie = imie_i_nazwisko[0]
        self.nazwisko = imie_i_nazwisko[1]

    def __str__(self) -> str:
        return f'{self.imie} {self.nazwisko}'

class Samolot:
    def __init__(self, max_predkosc: int, marka: str, model: str, numer):
        self.max_predkosc = max_predkosc
        self.marka = marka
        self.model = model
        self.numer = numer
    def dodaj_pilota(self):
        imie_i_nazwisko = str(input('Podaj imie i nazwisko pilota\n'))
        self.pilot = Pilot(imie_i_nazwisko)

    def __str__(self) -> str:
        return f'{self.marka}, {self.model}: {self.max_predkosc}\n' + self.pilot.__str__()


class Pas_startowy:
    def __init__(self) -> None:
        self.name = ''
class Hangar:
    
    def __init__(self) -> None:
        self.nazwa = random.randint(1,25)
        self.ilosc_miejsc = 5
        self.samoloty = [0 for j in range(self.ilosc_miejsc)]   

class Lotnisko:

    def __init__(self, ilosc_pasow) -> None:
        self.hangary = [Hangar() for i in range(random.randint(1,3))]
        self.pasy_startowe = [Pas_startowy() for j in range(ilosc_pasow)]

    def zmien_pilota_w_samolocie(self, nr_hangaru, nr_pietra, nr_pozycji):
        self.hangary[nr_hangaru].pietro[nr_pietra][nr_pozycji].dodaj_pilota()

# stworz lotnisko i hangar na moj_samolot i wstaw go do pierwszego hangaru na pierwsze pietro na piatej pozycji
def wypelnij_lotnisko(moje_lotnisko:Lotnisko):
    for j in range(len(moje_lotnisko.hangary)):
        for i in range(moje_lotnisko.hangary[j].ilosc_miejsc):
            moj_samolot = Samolot(random.randint(500, 600), 'TYT', 'stary', random.randint(1,1000))
            moj_samolot.dodaj_pilota()
            moje_lotnisko.hangary[j].samoloty[i] = moj_samolot
    return moje_lotnisko
def opisz_samoloty(lotnisko:Lotnisko):
    for j in range(len(lotnisko.hangary)):
        for i in range(len(lotnisko.hangary[j].samoloty)):
            samolot:Samolot = lotnisko.hangary[j].samoloty[i]
            print(f'Samolot numer {samolot.numer} z hangaru {lotnisko.hangary[j].nazwa} na miejscu {i+1} lata najszybciej {samolot.max_predkosc} i ma marke {samolot.marka} i jego model to {samolot.model}')
moje_lotnisko = Lotnisko(4)
wypelnij_lotnisko(moje_lotnisko)
opisz_samoloty(moje_lotnisko)
