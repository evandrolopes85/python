import random

#valor = random.randint(1,20)
#print('Gerar cinco números aleatórios entre 1 e 50: \n')
#for i in range(5):
#    n = random.randint(1,50)
#    print(f'Número gerado: {n}')

#valor = random.random(); # Gera numero aleatório entre z0 e 1
#print(f'Número gerado: {round(valor *10, 2)}') # com round eu arredondo o valor e o segundo argumento digo quantas casas decimais

#valor2 = random.uniform(1,100) # gera numero aleatório de ponto flutuante entre 1 e 100
#print(f'Número: {round(valor2, 4)}')

L = [2,4,6,9,10,13,14,16,18,20,21,27,33]
# n = random.choice(L) # vai escolher um dos números da lista
# print(n)

# n = random.sample(L, 3) # mostra 3 valores tirados aleatóriamente de dentro desta lista
# print(f'Números escolhidos: {n}')

#Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la')
n = random.shuffle(L)
print(L)