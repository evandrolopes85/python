#Modulo com funções variadas

#Função que exibe mensagem de boas-vidas:
def mensagem():
    print('Boson Treinamentos em técnologia!\n')

#Função para cálculo do fatorial de um número
def fatorial(numero):
    if numero < 0:
        return 'Digite um valor maior ou igual a zero'
    else:
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * fatorial(numero -1)

#Função para retornar uma série de fibonacci até um valor x:
def fibo(n):
    resultado = []
    a, b, = 0, 1
    while b <= n:
        resultado.append(b)
        a, b = b, a + b
    return resultado