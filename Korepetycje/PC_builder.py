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
class Komputer:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.czesci_komputera = []
    def enrgia_dodatnia(self):
        suma = 0
        for komponent in self.czesci_komputera:
            suma+=komponent.energia
        if suma>0:
            return True
        return False 
    def sprawdzanie_konfiguracji(self):
        if len(self.czesci_komputera)==3 and self.enrgia_dodatnia():
            print(f'Komputer "{self.nazwa}" działa😃')
        else:
            print(f'Komputer "{self.nazwa}" nie działa😥')
    def nieMaTakiegoTypu(self, typ):
        for komponent in self.czesci_komputera:
            if typ == type(komponent):
                return False
        return True
    def dodaj_komponent(self, komponent):
        if self.nieMaTakiegoTypu(type(komponent)):
            self.czesci_komputera.append(komponent)
        else:
            print(f'{type(komponent)} juz istnieje')
komputerDlaMieszka = Komputer('dla Mieszka')
komputerDlaMieszka.dodaj_komponent(Procesor('HG12', -200))
komputerDlaMieszka.dodaj_komponent(Zasilacz('SuperHS3', 700))
komputerDlaMieszka.dodaj_komponent(Pamiec('P1', -450))
komputerDlaMieszka.sprawdzanie_konfiguracji()