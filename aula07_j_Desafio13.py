salario = float(input('Digite o valor de seu salario R$'))
aumento = salario + (salario *0.15)
print('----------')
print('O valor do salario é R${:.2f}\nApós 15% de aumento o salário fica em R${:.2f}'.format(salario, aumento))