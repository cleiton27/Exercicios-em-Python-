#faça um programa que leia tres numeros e mostre
# qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = int
menor = int
meio = int

if(n1 > n2) and (n2 > n3):
    maior = n1
    meio = n2
    menor = n3
if(n2 > n1) and (n1 > n3):
    maior = n2
    meio = n1
    menor = n3
if(n3 > n1) and (n1 > n2):
    maior = n3
    meio = n1
    menor = n2
if(n3 > n2) and (n2 > n1):
    maior = n3
    meio = n2
    menor = n1
if(n2 > n1) and (n1 < n3) and (n1 > n3):
    maior = n2
    meio = n3
    menor = n1
if(n1 == n2) and (n2 == n3):
    maior = n1
    meio = n2
    menor = n3
print('==============================')
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

