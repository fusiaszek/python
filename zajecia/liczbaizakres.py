lista=[]
a=0
for i in range(10):
    x=input('podaj literke')
    lista.append(x)
listaunokatowa=[]
for j in lista:
    if j not in listaunokatowa:
        listaunokatowa.append(j)
print(lista)
print(listaunokatowa)
odwroconlistaunikatowa=[]
for u in listaunokatowa:
    a+=1
    odwroconlistaunikatowa.append(listaunokatowa[len(listaunokatowa)-a])
print(odwroconlistaunikatowa)