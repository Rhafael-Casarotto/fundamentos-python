print("Relatório de vendas!")
vendas = []
continuar = "s"

while continuar == "s":
    valor = float(input("Digite o valor da venda: R$"))
    vendas.append(valor)
    continuar = input("Deseja cadastrar uma nova venda? (s/n):").lower()

    while continuar != "s" and continuar != "n":
        continuar = input("Opção invalida. Digite s ou n:").lower()

print("\n---RESUMO---")
if len(vendas) > 0:
    total = sum(vendas)
    quantidade = len(vendas)
    media = total / quantidade
    
    print(f"Total vendido: R${total:.2f}")
    print(f"Quantidade de vendas: {quantidade}")
    print(f"Média por venda: R${media:.2f}")
    print("Vendas registradas:", vendas)
    
    print("A maior venda foi: ", max(vendas))
    print("A menor venda foi: ", min(vendas))

    vendas_acima_media = []

    for venda in vendas:
        if venda > media:
            vendas_acima_media.append(venda)

            vendas_acima_media.sort(reverse=True)       
            print("Vendas acima da média:", vendas_acima_media)
else:
    print("Nenhuma venda cadastrada.")












