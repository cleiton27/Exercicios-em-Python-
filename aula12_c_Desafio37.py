#Escreva um programa que leia um numero inteiro qualquer
# e peça para o usuario escolhar qual sera a base de conversao:
#1 para binario
#2 para octal
#3 para hexadecimal

numero = int(input('Digite um numero inteiro: '))
print('##### CONVERSOR DE BASES #####'
      '\n[ 1 ] BINARIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL')
base = int(input('Para qual base numerica voce quer converter? '))

if base == 1:
    print('O valor {} convertido para binario fica em {}: '
          .format(numero, bin(numero)[2:]))

elif base == 2:
    print('O valor {} convertido para octal fica em {}: '
          .format(numero, oct(numero)[2:]))

elif base == 3:
    print('O valor {} convertido para hexadecimal fica em {}: '
          .format(numero, hex(numero)[2:]))

else:
    print('Numero de base digitado fora do padrao.')