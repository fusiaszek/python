import random
import time

Tak_czy_Nie = input('tak czy nie? Czy chcesz żeby pomiędzy wynikami były przerwy 0.1 sekundowe?\n')
Ilosc_powtorzen_petli = int(input('Podaj ile razy chcesz żebym sprawdził kiedy się wylosują dwie takie same liczby:\n'))
lista = 0
for i in range(Ilosc_powtorzen_petli):
    if str.lower(Tak_czy_Nie) == 'nie':
        a = -1
        b = 1
        liczba_losowan = 0
        while a!=b:
            liczba_losowan+=1
            a = random.randint(-100,100)
            b = random.randint(-100,100)
        print(f'Udało się wylosować dwie takie same licby za {liczba_losowan} razem.')
        lista += liczba_losowan
    if str.lower(Tak_czy_Nie) == 'tak':
        a = -1
        b = 1
        liczba_losowan = 0
        while a!=b:
            liczba_losowan+=1
            a = random.randint(-100,100)
            b = random.randint(-100,100)
        print(f'Udało się wylosować dwie takie same licby za {liczba_losowan} razem.')
        lista += liczba_losowan
        time.sleep(0.1)
    if str.lower(Tak_czy_Nie) not in ['tak','nie']:
        exit(0)
print(f'Średnia liczba prób do wylosowania 2 takich samych liczb w losowych {Ilosc_powtorzen_petli} przypadkach wynosi {lista/Ilosc_powtorzen_petli}')