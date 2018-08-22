#leia o ano de nascimento de sete pessoas e mostre
# quantas nao atingiram a maio idade e quantas sao maiores de 21 anos
anoAtual = 2018
maiores = 0
menores = 7 - maiores
for a in range(1, 7):
    ano = int(input('Ano de nascimento: '))

if anoAtual - ano >= 21:
    maiores+=1

print('{} pessoas já são maiores de idade'.format(maiores))
print('{} pessoas são menores de idade'.format(menores))