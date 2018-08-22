#crie um programa que leia um numero e mostre na tela se ele é PAR ou IMPAR

numero = int(input('Digite um numero qualquer: '))

if(numero % 2 == 0):
    print('Você escolheu o numero {}, e ele é par'.format(numero))
else:
    print('Você escolheu o numero {}, e ele é impar'.format(numero))