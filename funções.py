lista_preco = [1500, 900, 1000, 8300]

# imposto
# aliquota1 - ir = 0.15
# aliquota2 - iss = 0.10
# aliquota3 - csll = 0.15

# exemplo de um calculo que iremos utilizar varias vezes no programa
# preco = 1500
# imposto_ir = 0.15 * preco
# imposto_iss = 0.10 * preco
# imposto_csll = 0.15 * preco
# imposto_total = imposto_ir + imposto_iss + imposto_csll
# print(f"O imposto total sobre o produto de R${preco} é: R${imposto_total}")
# def = 'define', a função desjada, nos (), o que ela vai receber para calcular

def calculo_imposto_total(preco): # posso add mais valores no ()
    if preco <= 2000:
        imposto_ir = 0.15 * preco
    else:
        preco > 2000
        imposto_ir = 0.30 *preco
    imposto_iss = 0.10 * preco
    imposto_csll = 0.15 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

# aliquota1 - ir = 0.15 sobre o produto até R$2000, acima, 0.30
for preco in lista_preco:
    imposto_total = calculo_imposto_total(preco)
    print(f"O imposto total sobre o produto de R${preco:.2f} é: R${imposto_total:.2f}")


nova_lista_produtos = [3000, 8000, 5400, 3322]

for preco in nova_lista_produtos:
    imposto_total = calculo_imposto_total(preco)
    print(f"O imposto total sobre o produto de R${preco:.2f} é de: R${imposto_total:.2f}")




