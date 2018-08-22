#desenvolva um programa que pergunte a distancia de uma viagem em km.
#calcule o preco da passagem, cobrando R$0,50 por km
# para viagens de ate 200km e R$0,45 para viagens mais longas

distancia = float(input('Qual será a distancia da viagem? '))
print('Sua viagem terá {} km'.format(distancia))


valorPassagem = float

if(distancia <= 200):
    valorPassagem = distancia * 0.50
else:
    valorPassagem = distancia * 0.45

print('==============================')
print('O valor da passagem é de R${:.2f}'.format(valorPassagem))