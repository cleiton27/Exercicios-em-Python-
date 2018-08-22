#Escreva um programa para aprovar o emprestimo bancario
# para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela nao pode
# exceder 30% do salario ou entao o emprestimo sera negado
print('##### BANCO PYTHON #####')
valorCasa = float(input('Qual o valor da casa?R$ '))
salario = float(input('Qual o valor de seu salario? '))
numeroAnos = int(input('Deseja pagar em quantos anos? '))

valorParcela = (valorCasa / (12 * numeroAnos))
minimo = salario * 30 / 100

print('O valor da parcela em {} anos, ficaria em {:.2f}'.format(numeroAnos, valorParcela))

if valorParcela <= minimo:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')





