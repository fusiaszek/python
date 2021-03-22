ciag=[1]
liczba=2
i=0
while liczba<4000000:
        ciag.append(liczba)
        poprzednia=ciag[i]
        przedpoprzednia = ciag[i - 1]
        liczba=(poprzednia)+(przedpoprzednia)
        i+=1
print(len(ciag))
print(ciag)
parzystesuma=0
for c in ciag:
    if c%2==0:
        parzystesuma+=c
print(parzystesuma)


