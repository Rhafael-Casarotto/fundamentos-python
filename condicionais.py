
# if condicao/comparacao:
#     # tudo o que acontece se a condição for verdadeira
# else:
#     # tudo o que acontece se a condição for falsa

vendas = 6000
meta = 5000
# principais comparadores
# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente

if vendas > meta:
    print("Vendedor bateu a meta")
    print("Vendedor recebera o bonus")
    bonus = 0.2 * vendas
    print("Bonus no valor de", bonus)
else:
    print("Vendedor não bateu a meta")
    print("Não sera efetuado pagamento da bonificação")


#exemplo2
vendas = 5800
meta1 = 4000 # bonus de 10%
meta2 = 5000 # bonus de 13%
meta3 = 6000 # bonus de 15%

if vendas >= 6000:
    bonus = 0.15 * vendas
else:
    if vendas >= 5000:
        bonus = 0.13 * vendas
    else:
        if vendas >= 4000:
            bonus = 0.10 * vendas
        else:
            bonus = 0

print("Bonus: ", bonus)

# outra forma de fazer

vendas = 6800
meta1 = 4000 # bonus de 10%
meta2 = 5000 # bonus de 13%
meta3 = 6000 # bonus de 15%

if vendas >= 6000:
    bonus = 0.15 * vendas
elif vendas >= 5000:
    bonus = 0.13 * vendas
elif vendas >= 4000:
    bonus = 0.10 * vendas
else:
    bonus = 0

print("Seu bonus sera de:", bonus)

# outro exemplo
lista_produtos = ["caneta", "lapis", "borracha", "caderno"]
produto_procurado = input("Pesquisar produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto em estoque")
else:
    print("Produto em falta")

# outro exemplo
vendas = 6800
vendas_empresa = 22000
meta_empresa = 20000
meta1 = 4000 # bonus de 10%
meta2 = 5000 # bonus de 13%
meta3 = 6000 # bonus de 15%

# se usar "or", uma das condições sera usada para dar o resultado, o "and", nesse caso, condiciona o resultado final.
if vendas >= 6000 and vendas_empresa >= meta_empresa:
    bonus = 0.15 * vendas
elif vendas >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 4000 and vendas_empresa >= meta_empresa:
    bonus = 0.10 * vendas
else:
    bonus = 0

print("Seu bonus sera de:", bonus)
