#Crie um programa que faça o computador jogar JOKENPO com voce
from random import randint
from time import sleep

computador = randint(1,3)

print('##### JOKENPÔ #####')
usuario = int(input('[1] - PEDRA:'
                    '\n[2] - PAPEL:'
                    '\n[3] - TESOURA:\n'
                    'Faça sua jogada: '))
print('JÓ..')
sleep(0.7)
print('KEN..')
sleep(0.7)
print('PÔ')

print('####################')

if usuario == 1 and computador == 1:
    print('Você escolheu PEDRA')
    print('O computador escolheu PEDRA')
    print('Jogo EMPATADO')

elif usuario == 2 and computador == 1:
    print('Você escolheu PAPEL')
    print('O computador escolheu PEDRA')
    print('Voce GANHOU')

elif usuario == 3 and computador == 1:
    print('Você escolheu TESOURA')
    print('Ocomputador escolheu PEDRA')
    print('Computador GANHOU')

elif usuario == 1 and computador == 2:
    print('Você escolheu PEDRA')
    print('O computador escolheu PAPEL')
    print('Computador GANHOU')

elif usuario == 2 and computador == 2:
    print('Você escolheu PAPEL')
    print('O computador escolheu PAPEL')
    print('Jogo EMPATADO')

elif usuario == 3 and computador == 2:
    print('Você escolheu TESOURA')
    print('Ocomputador escolheu PAPEL')
    print('Você GANHOU')

elif usuario == 1 and computador == 3:
    print('Você escolheu PEDRA')
    print('O computador escolheu TESOURA')
    print('Você GANHOU')

elif usuario == 2 and computador == 3:
    print('Você escolheu PAPEL')
    print('O computador escolheu TESOURA')
    print('Computador GANHOU')

elif usuario == 3 and computador == 3:
    print('Você escolheu TESOURA')
    print('Ocomputador escolheu TESOURA')
    print('Jogo EMPATADO')

else:
    print('Movimento INVALIDO')