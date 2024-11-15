import numpy as np

import mod_func as mf
#import numpy as mp

if __name__ == '__main__': #verifica se uma variavel especial intera do python do nome name é iqual este valor main. O __name__ é uma variável que tem no nome do modulo atual. pra evitar que partes do código seja executada antes da hhora
    mf.mensagem()
    num = int(input('Digite um numero inteiro positivo'))

    print(f'\nCalcular fatorial do numero:')
    fat = mf.fatorial(num)
    print(f'O fatorial é: {fat}')

    print(f'\nCalcular sequencia de fibonacci:')
    fib = mf.fibo(num)
    print(f'O fibonacci é: {fib}')

#   L = np.array([1,2,3,4,5,6,7,8,9])
#   print(L)