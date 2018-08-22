#Refaça o DESAFIo 009,
# mostrando a tabuada de um numero que o usuario escolher,
# só que agora utilizando o laço for
n = int(input('De qual numero voce quer a tabuada? '))
print('##########')
op = int(input('[1]SOMA\n[2]SUBTRAÇÃO\n'
               '[3]MULTIPLICAÇÃO\n[4]DIVISÃO\n'
               'Qual Operador para sua tabuada:'))

if op == 1:
    print('TABUADA DE SOMA DO NUMERO {}'.format(n))
    for m in range (1, 10):
        soma = m + n
        print('{} + {} = {}'.format(n, m, soma))
        m = m + 1
elif op == 2:
    print('TABUADA DE SOMA DO NUMERO {}'.format(n))
    for m in range (1, 10):
        sub = m - n
        print('{} - {} = {}'.format(n, m, sub))
        m = m + 1
elif op == 3:
    print('TABUADA DE SOMA DO NUMERO {}'.format(n))
    for m in range (1, 10):
        mult = m * n
        print('{} * {} = {}'.format(n, m, mult))
        m = m + 1
elif op == 4:
    print('TABUADA DE SOMA DO NUMERO {}'.format(n))
    for m in range (1, 10):
        div = m / n
        print('{} / {} = {}'.format(n, m, div))
        m = m + 1
