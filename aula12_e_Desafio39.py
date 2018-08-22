#Faça um programa que leia o ano de nascimento de um jovem
#e informe de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar
#se é a hora de se alistar
#se ja passou do tempo do alistamento
#seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
from datetime import date
anoAtual = date.today().year

print('##### ALISTAMENTO MILITAR #####')
print('[1] MASCULINO\n[2] FEMININO')
sexo = int(input('Digite o numero de seu sexo: '))

if sexo == 1:
    print('Sexo escolhido: MASCULINO')
    anoNascimento = int(input('Que ano voce nasceu? '))
    idade = anoAtual - anoNascimento

    if idade < 18:
        restante = 18 - idade
        print('Em {}, você esta com {} anos'.format(anoAtual, idade))
        print('Anda falta {} anos para voce se alistar'.format(restante))

    elif idade == 18:
        restante = 18 - idade
        print('Em {}, você esta com {} anos'.format(anoAtual, idade))
        print('Ja esta na hora de voce se alistar')

    elif idade > 18:
        restante = idade - 18
        print('Em {}, você esta com {} anos'.format(anoAtual, idade))
        print('Passou {} anos da data de voce se alistar'.format(restante))

    else:
        print('Digite um ano valido')
elif sexo == 2:
    print('Sexo escolhido: FEMININO')
    print('Seu alistamento não é obrigatório')

else:
    print('Opção Invalida')