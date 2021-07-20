WYMAGANE_KOMPONENTY = ['Procesor', 'Pamiec', 'Zasilacz', 'KartaGraficzna']

class Komponent:
    def __init__(self, nazwa, energia):
        self.nazwa = nazwa
        self.energia = energia


class Procesor(Komponent):
    def __init__(self, nazwa, energia):
        super().__init__(nazwa, energia)


class Pamiec(Komponent):
    def __init__(self, nazwa, energia):
        super().__init__(nazwa, energia)


class Zasilacz(Komponent):
    def __init__(self, nazwa, energia):
        super().__init__(nazwa, energia)


class HDD(Komponent):
    def __init__(self, nazwa, energia):
        super().__init__(nazwa, energia)


class KartaGraficzna(Komponent):
    def __init__(self, nazwa, energia):
        super().__init__(nazwa, energia)


class Komputer:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.czesci_komputera:Komponent = []

    def wypisz(self):
        print(f'Jestem komputerem o nazwie {self.nazwa}' )
        for komponent in self.czesci_komputera:
            print(f'posiadam {komponent.__class__.__name__} o nazwie {komponent.nazwa} o mocy {komponent.energia}')
    def enrgia_dodatnia(self):
        suma = 0
        for komponent in self.czesci_komputera:
            suma += komponent.energia
        if suma >= 0:
            return True
        return False 

    def sprawdzanie_konfiguracji(self):
        lista_czesci = [komponent.__class__.__name__ \
            for komponent in self.czesci_komputera]
        #print(lista_czesci)
        #print(lista_czesci == WYMAGANE_KOMPONENTY)
        lista_spelniona = True
        for czesc in WYMAGANE_KOMPONENTY:
            if czesc not in lista_czesci:
                lista_spelniona = False
                break
        
        if self.enrgia_dodatnia() and lista_spelniona:
            print(f'Komputer "{self.nazwa}" działa😃')
        else:
            print(f'Komputer "{self.nazwa}" nie działa😥')

    def sprawdz_czy_nie_ma_komponentu(self, typ):
        for komponent in self.czesci_komputera:
            if typ == type(komponent):
                return False
        return True

    def dodaj_komponent(self, komponent):
        if self.sprawdz_czy_nie_ma_komponentu(type(komponent)):
            self.czesci_komputera.append(komponent)
            self.sprawdzanie_konfiguracji()
        else:
            print(f'{type(komponent)} juz istnieje')

class User:
    moje_komputery = []

    def __init__(self, imie) -> None:
        self.imie = imie

    def dodaj_komputer(self, komputer: Komputer):
        self.moje_komputery.append(komputer)
    
    def usun_komputer(self, indeks: int):
        self.moje_komputery.pop(indeks)

    def usun_wszystkie_komputery(self):
        self.moje_komputery.clear()
    
    def wypisz(self):
        print(f'jestem uzytkownikiem o imieniu "{self.imie}"')

class KomputerBuilder:
    def __init__(self, user: User) -> None:
        self.user = user.imie

class interfejs_uzytkownika():
    komputery:Komputer = []
    uzytkownicy:User = []
    def __init__(self) -> None:
        print('Hello')
    def stworz_uzytkownika(self):
        nowy = User(input('podaj imie\n'))
        self.uzytkownicy.append(nowy)
    def stworz_komputer(self):
        nazwa_komputera = input('podaj nazwe komputera\n')
        procesor_nazwa = input('podaj nazwe procesora\n')
        energia_procesora = int(input('podaj energie procesora\n'))
        HDD_nazwa = input('podaj nazwe HDD\n')
        energia_HDD = int(input('podaj energie HDD\n'))
        zasilacz_nazwa = input('podaj nazwe zasilacza\n')
        energia_zasilacza = int(input('podaj energie zasilacza\n'))
        pamiec_nazwa = input('podaj nazwe pamieci\n')
        energia_pamieci = int(input('podaj energie pamieci\n'))
        kartagraficzna_nazwa = input('podaj nazwe karty graficznej\n')
        energia_kartygraficznej = int(input('podaj energie karty graficznej\n'))
        komputer = Komputer(nazwa_komputera)
        komputer.dodaj_komponent(Procesor(procesor_nazwa,energia_procesora))
        komputer.dodaj_komponent(HDD(HDD_nazwa,energia_HDD))
        komputer.dodaj_komponent(Zasilacz(zasilacz_nazwa,energia_zasilacza))
        komputer.dodaj_komponent(Pamiec(pamiec_nazwa,energia_pamieci))
        komputer.dodaj_komponent(KartaGraficzna(kartagraficzna_nazwa,energia_kartygraficznej))
        self.komputery.append(komputer)
    def wyswietl_swoje_komputery(self):
        for komputer in self.komputery:
            komputer.wypisz()
    def wyswietl_swojich_uzytkownikow(self):
        for uzytkownik in self.uzytkownicy:
            uzytkownik.wypisz()
    def wypisz_menu(self):
        print('''1.stworz uzytkownika
        2.zbuduj komputer
        3.wyswiet swoje komputery i swojich uzytkownikow''')
    def podaj_numer(self) -> int:
        return int(input('podaj numer\n'))

uzytkownik = User("Mieszko")


komputerDlaMieszka = Komputer('dla Mieszka')
komputerDlaMieszka.dodaj_komponent(Procesor('HG12', -200))
komputerDlaMieszka.dodaj_komponent(HDD('HDD1', -50))
komputerDlaMieszka.dodaj_komponent(Zasilacz('SuperHS3', 1200))
komputerDlaMieszka.dodaj_komponent(Pamiec('P1', -450))
komputerDlaMieszka.dodaj_komponent(KartaGraficzna('RTX 3090', -400))

uzytkownik.dodaj_komputer(komputerDlaMieszka)
interfejs = interfejs_uzytkownika()
while True:
    interfejs.wypisz_menu()
    co_wybral = interfejs.podaj_numer()
    if co_wybral == 1:
        interfejs.stworz_uzytkownika()
    if co_wybral == 2:
        interfejs.stworz_komputer()     
    if co_wybral == 3:
        interfejs.wyswietl_swoje_komputery()
        interfejs.wyswietl_swojich_uzytkownikow()
