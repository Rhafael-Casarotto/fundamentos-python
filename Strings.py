faturamento = 1500
custo = 300
lucro = faturamento - custo
margem_lucro = lucro/faturamento

# "f" para formatar strings de forma legivel. Dentro das "{}"

print(f"Faturamento: {faturamento} , Custo: {custo} Lucro: {lucro}")

email_cliente = "intel@gmail.com"

# maiusula = upper
email_cliente = email_cliente.upper()
print(email_cliente)

# minuscula = lower
email_cliente = email_cliente.lower()
print(email_cliente)

# achar um caracter [:5]
print(email_cliente [:5])

# trocar um pedaço do texto = replace
novo_email = email_cliente.replace ("gmail.com", "outlook.com")
print(novo_email)

# procurar especifico, ex:"@"= find
# encontrar o servidor após @
posicao_arroba = email_cliente.find("@")
servidor = email_cliente[posicao_arroba:]
print(servidor)

# maiusculas e minusculas
nome = "rhafael paim"
# encontrar o espaço
posicao_espaco = nome.find(" ")
# usar [texto anterior: variavel]
primeiro_nome = nome[:posicao_espaco]
# usar [variavel+1: texto subsequente]
sobrenome = nome[posicao_espaco+1:]
# title = primeira letra maiuscula das palavras
# captalize = primeira letra maiuscula do texto
print(nome.title())
print(primeiro_nome.title())
print(sobrenome.title())

# casos especiais, formatação numerica.
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento: R${faturamento:.2f} , Custo: R${custo:.2f} Lucro: R${lucro:.2f}, Margem: {margem_lucro:.0%}")
# o codigo :.2f sinaliza os numeros decimais, chamados float
# em {margem_lucro:.0%}, o ":" indica que ainda quero formatar