# 1. Algorytm mnożenia dwóch liczb nieujemnych całkowitych przy pomocy dodawania
# 2. Algorytm dzielenia z resztą dwóch liczb całkowitych (nieujemnej przez dodatnią) przy pomocy odejmowania
# 3. Zsumować 1000 kolejnych liczb nieparzystych zaczynając od 7 (ogólnie zsumować N kolejnych liczb nieparzystych
# zaczynając od K)
# 4. Napisać program sumujący liczby dwucyfrowe podzielne przez 7
def zadanie1(liczba1,liczba2):
    # range(
    wynik=0
    for i in range(liczba2):
        wynik+=liczba1
    print(wynik)
zadanie1(3,9)

# 6   3
# 6 - 3 = 3 calosci += 1
# 3 - 3 = 0 calosci += 1
# 0 - 3 = -3
def zadanie2(liczba1,liczba2):
    calosci=0
    while liczba1 >= 0:
        liczba1 -= liczba2
        calosci += 1
    print("Calosci: ", calosci-1)
    print("Reszta: ", liczba1+liczba2)

zadanie2(25,7)

def zadanie3():
    suma=0
    k = 7
    for i in range(1000): # [7,8,9,10,...,1000] [7,9,11,13,15,17,...,2007]
        suma += k
        k+=2
    print(suma)

zadanie3()

# 4. Napisać program sumujący liczby dwucyfrowe podzielne przez 7
def zadanie4():
    suma=0
    for i in range(10,100):
        if i%7==0:
            suma+=i

    print(i)
zadanie4()