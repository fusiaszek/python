wyraz=str(input('Podaj wyraz '))
wyraz=wyraz.replace(' ','')
dlugosc=len(wyraz)
rozmiar=0
for i in range(dlugosc):
    if wyraz[i]==wyraz[dlugosc-i-1]:
        rozmiar+=1
if rozmiar==dlugosc:
    print(True)
if rozmiar!=dlugosc:
    print(False)