#Refaça o desafio 35 dos triangulos, acrescentando recurso de
# mostrar que tipo de triangulo sera formado:
#Equilatero: todos os lados iguais
#Esosceles: dois lados iguais
#Escaleno: todos os lados diferentes

print('Analisando o Triângulo')
print('==============================')
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if(a < b + c) and (b < a + c) and (c < a + b):
    print('==============================')
    print('As medidas formam um triangulo ', end='')
    if (a == b == c):
        print('EQUIULATERO')
    elif (a != b != c != a):
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('==============================')
    print('As medidas não formam um triangulo')

#cada segmento tem que ser menor do que a soma do outros lados