plik=open('farby.txt', 'r')
linie=plik.readline().split(' ')
max=int(linie[0])
dosypywanie=int(linie[1])
puszki=[''] * max
print(puszki)
for i in range(dosypywanie):
    linia=(plik.readline().split(' '))
    a=int(linia[0])
    b=int(linia[1])
    barwnik=linia[2]
    for puszka in range(a-1,b):
        if barwnik!=0:
            puszki[puszka]+=barwnik.replace('\n','')
print(puszki)
ilosc=0
for puszka in puszki:
    if puszka.count('1')>0 and puszka.count('2')>0 and puszka.count('3')==0:
        ilosc+=1
print('Powstalo {0} puszek farby zielonej'.format(ilosc))