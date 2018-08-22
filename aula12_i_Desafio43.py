#Desenolva uma logica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5 abaixo do peso
#Entre 18.5 e 25 Peso ideal
#25 ate 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obesidade morbida
from math import sqrt
print('##### CALCULO IMC #####')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('IMC: {:.2f} voce está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.2f} voce está no peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.2f} voce está com sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('IMC: {:.2f} voce está com obesidade'.format(imc))
else:
    print('IMC: {:.2f} voce está com obesidade morbida'.format(imc))