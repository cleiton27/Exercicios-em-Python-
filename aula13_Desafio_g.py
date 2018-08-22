#faça um programa que leia um numero inteiro e diga se ela é ou nao um numeo primo

numero = int(input('Qual numero: '))
cont = 0
for a in range (1, numero+1):
    if numero % a == 0:
        print('\033[38m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(a), end=' ')

print('\n\033[mO numero {} foi dividido {} vezes'.format(numero, cont))

if cont == 2:
    print('Numero primo')
else:
    print('Numero nao primo')
