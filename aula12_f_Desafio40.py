#crie um programa que leia duas notas de um aluno e calcule sua media
#mostrando uma mensagem no final, de acodo com a media atingida
#media abaixo de 5.0 REPROVADO
#media etnre 5.0 e 6.9 RECUPERAÇÂO
#media 7.0 ou superior APROVADO
print('##### SISTEMA DE CALCULO DE MEDIA #####')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

if media < 5.0:
    print('REPROVADO')
elif media == 5.0 or media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')