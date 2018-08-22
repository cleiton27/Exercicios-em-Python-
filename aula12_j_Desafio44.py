#elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#a vista dinheiro/cheque: 10% de desconto
#a vita no cartao: 5% de desconto
#em ate 2x no cartao: preço normal
#3x ou mais no cartao: 20% de juros

produto = float(input('Qual o valor do produto? '))
dinheiro = 0

pagamento = float(input('##### COMPRAS #####'
                        '\n[1] - A vista no dinheiro ou cheque:'
                        '\n[2] - A vista no cartão:'
                        '\n[3] - Em até 2x no cartão:'
                        '\n[4] - Em 3x ou mais no cartão:'
                        '\nQual a forma de pagamento?'))
print('##############################')

if pagamento == 1:
    dinheiro = produto - (produto * 0.10)
    print('Pagamento escolhido A VISTA NO DINHEIRO'
          '\nO valor do produto fica em {:.2f}'.format(dinheiro))

elif pagamento == 2:
    dinheiro = produto - (produto * 0.05)
    print('Pagamento escolhido A VISTA NO CARTAO')
    print('O valor do produto fica em {:.2f}'.format(dinheiro))

elif pagamento == 3:
    dinheiro = produto
    print('Pagamento escolhido em ate 2x NO CARTAO')
    print('O valor do produto fica em {:.2f}'.format(dinheiro))

elif pagamento == 4:
    dinheiro = produto + (produto * 0.20)
    print('Pagamento escolhido em 3x ou mais NO CARTAO')
    print('O valor do produto fica em {:.2f}'.format(dinheiro))

else:
    print('Forma de pagamento invalida.')
