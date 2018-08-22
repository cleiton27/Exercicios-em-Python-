#escreva um programa que pergunte o salario de um funcionario e calcule
# um aumento de 10% para salarios maiores a R$1250 e
# um aumento de 15% para os menores ou iguais

salario = float(input('Digite o valor do salário R$'))

if(salario > 1250):
    porcentagem = '10%'
    aumento = salario * 0.10
    novoSalario = salario + aumento

else:
    porcentagem = '15%'
    aumento = salario * 0.15
    novoSalario = salario + aumento
print('==============================')
print('O salario digitado foi de R${}'.format(salario))
print('Com isso você recebeu um aumento de R${}'.format(aumento))
print('Após o aumento de {} o salario ficou em R${}'.format(porcentagem,novoSalario))