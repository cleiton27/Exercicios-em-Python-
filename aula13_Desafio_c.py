#faça um programa que calcule a soma
# ente todos os numeros impares que
# sao multiplos de tres e que se
# encontram no intervalo de 1 ate 500
soma = 0
for c in range (1, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
print('A soma dos numeros impares entre 1 e 500 é {}'.format(soma))