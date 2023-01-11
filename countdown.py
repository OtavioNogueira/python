from time import sleep 
from datetime import date

ano = date.today().year

for i in range (10, 0, -1):
  print(i)
  sleep(1.2)

print('FELIZ {}!!!'.format(ano+1))