from random import randrange;
print("Cześć. Wymyślę liczbę z zakresu od 0 do tej którą wskażesz a potem będziesz musiał ją zgadnąć :)");
zakres = int(input("Podaj do jakiej liczby od 0 mam losować: "));
print("Wymyślam liczbę od 0 do " + str(zakres) + " zgadnij jaka to liczba");
liczba = randrange(zakres);
a = -1;
proba = 0;
while a != liczba:
	a = int(input("Podaj propozycję:"));
	if a < liczba: print("za mało");
	if a > liczba: print("za dużo");
	if a == liczba: print("zgadłeś");
	proba += 1;
print("Zgadłeś za " + str(proba) + " razem");
imie = input("Jak masz na imie (what is your name) ?:");
file = open("wyniki.txt", "a+");
file.write(imie + " zgadl za " + str(proba) + " razem liczbe " + str(liczba) + " z zakresu od 0 do " + str(zakres) + "\n");
file.close();
print("Aktualne wyniki:");
file = open("wyniki.txt", "r");
lines = file.readlines();
for line in lines:
	print(line);
file.close();

