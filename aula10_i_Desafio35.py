#desenvolva um programa que leia o comprimento de tres retas
#e diga ao usuario se elas podem ou nao formar um triangulo
print('Analisando o Triângulo')
print('==============================')
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if(a < b + c) and (b < a + c) and (c < a + b):
    print('==============================')
    print('As medidas formam um triangulo')
else:
    print('==============================')
    print('As medidas não formam um triangulo')

#cada segmento tem que ser menor do que a soma do outros lados