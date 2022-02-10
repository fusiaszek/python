n = int(input())
liczba = ''
while True:
        liczba += str(n % 5)
        n = int(n/5)
        if n == 0:
            break
liczba = liczba[::-1]
print(int(liczba)*2)