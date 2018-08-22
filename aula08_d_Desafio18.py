import math

valor = float(input('Digite o valor de um angulo qualquer: '))

seno = math.sin(math.radians(valor))
cosseno = math.cos(math.radians(valor))
tangente = math.tan(math.radians(valor))

print('Seno {:.2f} '.format(seno))
print('Cosseno {:.2f} '.format(cosseno))
print('Tangente {:.2f} '.format(tangente))

