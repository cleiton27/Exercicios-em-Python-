#escreva um programa que leia a velocidade de um carro
#se ultrapassar 80KM/h mostre uma mensagem dizento que ele foi multado
#a multa vai custar R$7,0 por cada km acima do limite

velocidade = float(input('Digite a velocidade do carro: '))
velPermitida = 80.0
limite = velocidade - velPermitida
multa = limite * 7.0

if(velocidade > velPermitida):
    print('Dirija com segurança')
    print('Você foi multado em R${}'.format(multa))

else:
    print('Dirija com segurança')
    print('Você não foi multado')
