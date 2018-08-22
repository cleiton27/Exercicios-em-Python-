import math

oposto = float(input('Digite a medida do cateto oposto: '))
adjacente = float(input('Digite a medida do cateto adjacente: '))
hipo = math.hypot(oposto, adjacente)
print('A medida da hipotenusa é {:.2f} '.format(hipo))