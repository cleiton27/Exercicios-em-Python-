preco = float(input('Digite o valor do produto: R$ '))
desconto = preco - (preco * 0.05)
print('----------')
print('O valor do produto é R${:.2f}\nApós o desconto de 5% o valor fica em R${:.2f} '.format(preco, desconto))