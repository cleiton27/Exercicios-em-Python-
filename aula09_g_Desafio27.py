nome = input('Digite o seu nome: ').strip()
primeiro_nome = nome.split()


print('Muito prazer em ti conhecer')
print('Seu primeiro nome é {}'.format(primeiro_nome[0]))
print('Seu ultimo nome é {}'.format(primeiro_nome[len(primeiro_nome)
                                                  - 1]))

