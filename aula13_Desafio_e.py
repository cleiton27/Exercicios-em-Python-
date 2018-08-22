#Desenvolva um programa que leia seis numeros inteiros e mostre
#a soma apenas daqueles que forem pares, se o valor for impar
#desconsidere
a = 0
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
       a = a + n
print('A soma entre os numeoros pares é {}'.format(a))