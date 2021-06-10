#from Korepetycje.zdrowiebmi import BMR
import math
from os import PathLike
from re import T

masaciala = 80.
plec = 'm'
wzrost = 190
wiek = 25
wspl_aktywnosc = 1.2

def pobierz_dane_od_uzytkownika():
    # pobierz wage, wzrost, plec, wiek i wspolczynnik aktywnosci (w zadaniu BAF)
    global masaciala
    masaciala = float(input('jaka masz mase ciala\n'))

    global plec
    plec = input('jak masz plec (k lub m)\n')

    global wzrost
    wzrost = float(input('ile masz wzrostu\n'))

    global wiek
    wiek = float(input('ile masz lat\n'))

    global wspl_aktywnosc
    opcja = int(input('''Wybierz wspolczynnik aktywnosci
    (1) = 1.2
    (2) = 1.375
    (3) = 1.55
    (4) = 1.725
    (5) = 1.9\n'''))
    if opcja == 1:
        wspl_aktywnosc = 1.2
    elif opcja == 2:
        wspl_aktywnosc = 1.375
    elif opcja == 3:
        wspl_aktywnosc = 1.55
    elif opcja == 4:
        wspl_aktywnosc = 1.725
    elif opcja == 5:
        wspl_aktywnosc = 1.9
    else:
        wspl_aktywnosc = 1.2

def policz_bmi():
    # waga / wzrost_w_metrach^2
    bmi = masaciala / math.pow(wzrost / 100, 2)
    print(f"Twoje BMI wynosi {bmi:.2f}")
    if bmi < 18.5:
        print('niedowaga!')
    elif bmi >= 18.5 and bmi < 25:
        print('optimum')
    elif bmi >= 25.0 and bmi < 30:
        print('nadwaga')
    elif bmi >= 30.0 and bmi < 40.0:
        print('otylosc!')
    return bmi

def policz_bmr():
    if plec == 'm':
        BMR = (10*masaciala) + (6.25*wzrost) - (5*wiek) + 5
    else:
        BMR = (10 * masaciala ) + (6.25 * wzrost) - (5 * wiek) - 161
    return BMR

def policz_tdee():
    tdee = policz_bmr() * wspl_aktywnosc
    return tdee
    
def zapisz_do_pliku(bialko,wegle,tluszcze):
    plik = open('mikroskladniki.txt','w')
    plik.write(' \tbialko\twegle\ttluszcze\n')
    plik.write(f'kCal\t{bialko / 0.14}\t{wegle / 0.14}\t{tluszcze / 0.14}\n')
    plik.write(f'g\t{bialko}\t{wegle}\t{tluszcze}')
    plik.close()
# ile kalorii i ile gram konkretnych makroskladnikow (weglowodany, bialka i tluszcze)
def policz_makroskladniki():
    bialko = 1.1 * masaciala
    wegle = 0.14 * policz_bmr() * 0.5
    wszystko = wegle * 2
    tluszcze = wszystko - bialko - wegle

    print('Musisz jesc ' + str(bialko) + 'g bialka')
    print('Musisz jesc ' + str(wegle) + 'g weglowodanow')
    print('Musisz jesc ' + str(tluszcze) + 'g tluszczy')

    zapisz_do_pliku(bialko,wegle,tluszcze)

# uruchamia wszystkie funkcje i nimi steruje/dostosowywuje
def main():
    pobierz_dane_od_uzytkownika()
    policz_makroskladniki()
    policz_bmi()
    print(f"Twoje BMR wynosi {policz_bmr()}")
    print(f"Twoje TDEE wynosi {policz_tdee()}")

main()