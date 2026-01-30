# for = usado para fazer repetições no Python

lista_vendas = [1200, 900, 2300, 1450, 2550]
meta = 1200
bonus = 0.1

# duas maneiras de usar o "for"
# for i in range(10):
# i = indice   10 = quantas vezes vai rodar o cod

# para cada item da lista
# linhas de cod dentro do for, para executar varias vezes
for vendas in lista_vendas:
    print(vendas)
    if meta <= vendas:
        bonus = 0.1 * vendas
        print("Seu bonus é de: ", bonus)
    else:
        print("Não atingiu a meta")
# fiquei feliz em fazer essa linha de codigo sozinho, pois analisei o estudo de ontem, as condicionais e incorporei no cod.




