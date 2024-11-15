while(True):
    dados = input()
    if(len(dados) > 2 and):
        D = dados.split(" ")[0]
        N = dados.split(" ")[1]
        continue

    if(int(D) == 0 and int(N) == 0):
        break
    else:
        saida = N.replace(str(D), "")
    
        print(f'{int(saida)}')
    
        dados = ""
