#a confederação nacional de natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
#ate 9 anos: MIRIM
#ate 14 anos: INFANTIL
#ate 19 anos: JUNIOR
#ate 20 anos: SENIOR
#acima: MASTER
from datetime import date
print('##### SISTEMA DE CATEGORIA PARA NATAÇÃO #####')

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano que voce nasceu: '))
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Voce tem {} anos}'.format(idade))
    print('Categoria: MIRIM')

elif idade > 9 and idade <= 14:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: INFANTIL')

elif idade > 14 and idade <= 19:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: JUNIOR')

elif idade == 20:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: SENIOR')

else:
    print('Voce tem {} anos'.format(idade))
    print('Categoria: MASTER')