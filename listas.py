#listas
#posição   0    1    2    3    4   -1 ou 5
vendas = [150, 262, 665, 365, 458, 663]

#soma dos elementos
total_vendas = sum(vendas)
print("Total das vendas: ",total_vendas)

#tamanho da lista, usar len, como em textos
quantidade_vendas = len(vendas)
print("Total de vendas efetuadas: ",quantidade_vendas)

# max e min
print("A maior venda foi:",max(vendas))
print("A menor venda foi:",min(vendas))

#pegar posição
print(vendas[0])

lista_produtos = ["caderno", "lapis", "caneta", "borracha"]
#para não rodar o input, deixar em comentario
# produto_procurado = input("Pesquise o produto: ")
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produtos)

#adicionar um item
lista_produtos.append("estojo")
print(lista_produtos)

#remover um produto
lista_produtos.remove("borracha")
print(lista_produtos)

# lista_produtos.pop(0), para remover item da posição

#editar um item
# precos = [1000, 2350, 4000]
# precos[0] = precos[0] * 2.5
# print(precos)

#contagem de itens na lista
lista_produtos = ["caderno", "lapis", "caneta", "borracha", "borracha", "lapis", "lapis"]
print(lista_produtos.count("lapis"))

#ordenar lista
lista_produtos.sort()
print(lista_produtos)
# lista_produtos.sort(reverse=True), para ordenar ao contrario
