listazakupow=[]
warzywo=''
minus=''
while warzywo!='x':
    warzywo=input('podaj produkt ')
    minus=input('co chcesz usunac jak tak to podaj nazwe a jak nie to napisz nic ')
    zamien=input('jesli chcesz cos zamienic to napisz nazwe tego produktu a jak nie to napisz nic ')
    if warzywo!='x':
        listazakupow.append(warzywo)
    if zamien!='nic':
        druganazwa=input('podaj nowa nazwe produktu ')
        listazakupow.remove(zamien)
        listazakupow.append(druganazwa)
    if minus=='nic':
        print('')
    if minus!='nic':
        listazakupow.remove(minus)
print('to twoja lista zakupow'+str(listazakupow))