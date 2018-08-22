valor = float(input('Digite quanto dinheiro você tem? R$ '))
dolar = valor / 3.27
print('Você tem R${:.2f} em sua carteira, em dolares você tem US${:.2f}'.format(valor, dolar))