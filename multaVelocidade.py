v = int(input('Qual sua velocidade: '))

multa = (v-80) * 7 

if v > 80:
  print("Você foi multado em R${}".format(multa))