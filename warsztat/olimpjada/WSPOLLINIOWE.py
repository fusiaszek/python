a = input()
lista = a.split("\t")
x1 = int(lista[0])
y1 = int(lista[1])
x2 = int(lista[2])
y2 = int(lista[3])
x3 = int(lista[4])
y3 = int(lista[5])

if (x2 - x1) * (y3 - y2) == (y2 - y1) * (x3 - x2):
    print("są")
else:
    print("nie są")