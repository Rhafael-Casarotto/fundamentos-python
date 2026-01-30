# codigo para estudo pratico
lista_vendas = []
meta = 5000
for i in range(3):
    valor = float(input(f"Digite o valor da venda {i+1}:"))
    lista_vendas.append(valor)

total_vendas = sum(lista_vendas) 
media = total_vendas / len(lista_vendas)

print("Relatório de vendas.")
print(f"Total de vendas: {len(lista_vendas)}")
print(f"Total em vendas: {total_vendas:.2f}")
print(f"Media por vendas: {media:.2f}")

if meta <= total_vendas:
    print("Meta concluida, equipe recebe bonus!")
else:
    print("Meta não concluida.")








