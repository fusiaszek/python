# ciag=[0]
# for i in range(10):
#     poprzednia=ciag[i]
#     liczba=(poprzednia+1)+(poprzednia+2)
#     ciag.append(liczba)
# print(ciag)

ciag=[1,2]
t=0
for i in range(1,10):
    while ciag[i]<1000:
        if ciag[i]%2==0:
            t+=ciag[i]
        poprzednia=ciag[i]
        liczba=(poprzednia)+(ciag[i-1])
        ciag.append(liczba)
print(t)

