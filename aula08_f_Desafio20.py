import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

sorteio = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sorteio)
#shuffle embaralha a lista
print('O aluno sorteado foi o {} '.format(sorteio))

