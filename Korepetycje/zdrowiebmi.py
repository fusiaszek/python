

masaciala = float(input('jaka masz mase ciala'))
plec = input('jak masz plec (k lub m)')
wzrost = float(input( 'ile masz wzrostu'))
wiek = float(input('ile masz lat '))

BMR = 0

if plec == 'm':
    BMR = (10*masaciala) + (6.25*wzrost) - (5*wiek) + 5

if plec == 'k' :
    BMR = ( 10 * masaciala ) + ( 6.25 * wzrost ) - ( 5 * wiek ) - 161

print ( 'BMR to ' + str ( BMR ) + ' kCal' )

BMI = masaciala / wzrost / wzrost * 10000

print ('BMI to ' + str ( BMI ) )

if BMI < 18.5:
    print('niedowaga!')

if BMI >= 18.5 and BMI < 25:
    print('optimum')

if BMI >= 25.0 and BMI < 30:
    print('nadwaga')

if BMI >= 30.0 and BMI < 40.0:
    print('otylosc!')

schudnac = BMR - ( BMR * 0.07 )
przytyc = BMR + ( BMR * 0.07 )
print('Aby schudnac ' + str(schudnac) + ' kCal')
print('Aby przytyc ' + str(przytyc) + ' kCal')

bialko = 1.1 * masaciala
wegle = 0.14 * BMR * 0.5
wszystko = wegle * 2
tluszcze = wszystko - bialko - wegle

print('Musisz jesc ' + str(bialko) + 'g bialka')
print('Musisz jesc ' + str(wegle) + 'g weglowodanow')
print('Musisz jesc ' + str(tluszcze) + 'g tluszczy')