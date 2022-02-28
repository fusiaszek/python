n = input()
liczba_domkow = int(n[0])
wiersz1 = n[1].split()
for i in range(2,liczba_domkow+1):
    wiersz = n[i].split()
    b = int(wiersz[0]) + int(wiersz1[1]) 
    c = int(wiersz[0]) + int(wiersz1[2]) 
    najmniejsza = b
    if c < najmniejsza:  
        najmniejsza = c
    a1 = najmniejsza

    wiersz = n[i].split()
    a = int(wiersz[1]) + int(wiersz1[0]) 
    c = int(wiersz[1]) + int(wiersz1[2]) 
    najmniejsza = a
    if c < najmniejsza:  
        najmniejsza = c
    b1 = najmniejsza

    wiersz = n[i].split()
    a = int(wiersz[2]) + int(wiersz1[0]) 
    b = int(wiersz[2]) + int(wiersz1[1])  
    najmniejsza = a
    if b < najmniejsza:
        najmniejsza = b
    c1 = najmniejsza

    wiersz1[0] = a1
    wiersz1[1] = b1
    wiersz1[2] = c1

najmniejsza = wiersz1[0]
if wiersz1[1] < najmniejsza:
    najmniejsza = wiersz1[1]
if wiersz1[2] < najmniejsza:
    najmniejsza = wiersz1[2]  
print(najmniejsza)