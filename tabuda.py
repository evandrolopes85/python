valor = int(input('Digite um valor: '))

for index in range(1, 11):
    print(f'{valor} X {index:2} = {valor * index:>2}')