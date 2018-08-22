#Faça um programa que mostre na tela uma contagem regressiva
#  para o estouro de fogos de artificio,
# indo de 10 ate 0, com uma pausa de um segundo entre eles
from time import sleep
print('CONTAGEM REGRESSIVA PARA OS FOGOS')
print('####################')
i = 10
for c in range(i, 0, -1):
    print(c)
    sleep(1)
print(' *\*|*/* FOGOS *\*|*/* ')