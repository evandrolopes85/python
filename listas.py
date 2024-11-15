# Lista: representa uma sequência de valores

# Sintaxe: nome_lista = [valores]

#notas = [5,7,8,6,9]
#print(notas)

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,4]
valores = n1 + n2
#print(valores)
#print(type(valores))

print(valores[-2]) # acessar o primeiro valor da lista, -1 significa o ultimo valor da lista ( o sinal de menos acessa do final para o começo )

valores[0] = 9

print(valores[0])

# Acessar os valores sequenciais de uma lista com a operação slace
print(valores[3:6]) # acessa apartir da posicao 0 dois valores

# sabe o tamanho da lista
print(len(valores))

# ordenar a lista
print(sorted(valores)) # retorna uma nova lista ordenada
print(sorted(valores, reverse=True)) # retorna a lista invertida
print(sum(valores)) # somar todos os valores da lista
print(min(valores)) # recuperar o menor valor
print(max(valores)) # recuperar o maior valor

valores.append(13) # acrescentar um valor a lista
print(valores)
valores.pop() # remover o ultimo elemento da lista
print(valores)
valores.pop(3) # remover o elemento da posicao 3
print(valores)
valores.insert(3,21) # inserir valores em uma posicao especifica, posicao virgula valor
print(valores)

print(17 in valores)# verfifica se existe valores na lista