#

palindromos = []
for i in range(100, 1000):
    for n in range(100, 1000):
        ''' outra solução:
        funçao que cria lista cujos elementos são os caracteres da string
        função para reordenar a lista e colocala ao contrario
        função para concatenar todos os elementos da lista em uma strint
        '''
        if f"{i * n}" == f"{i * n}"[::-1]:
            print(f"{i * n}", f"{i * n}"[::-1])
            palindromos.append(i * n)
print(palindromos)