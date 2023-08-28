valor = float(input())

cem = valor//100 
cem2 = valor%100 

cin = cem2//50
cin2 = cem2%50

vin = cin2//20 
vin2 = cin2%20

de = vin2//10 
de2 = vin2%10

ci = de2//5 
ci2 = de2%5

do = ci2//2
do2 = ci2%2

um = ci2//1



print('{:.0f} nota(s) de R$100'.format(cem))
print('{:.0f} nota(s) de R$50'.format(cin))
print('{:.0f} nota(s) de R$20'.format(vin))
print('{:.0f} nota(s) de R$10'.format(de))
print('{:.0f} nota(s) de R$5'.format(ci))
print('{:.0f} nota(s) de R$2'.format(do))
print('{:.0f} nota(s) de R$1'.format(um))
