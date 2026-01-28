# .py = extensão python, facilita.
# todo texto dentro da programação ("texto")
# codigo vai ser executado, de cima para baixo.

# criando uma variavel, ele vai ser o nome do numero.

faturamento = 4200
custo = 1500
novas_vendas = 600
# sempre usar ponto, não virgula nos numeros
# calculo de porcentagem no cod
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.2
# 0.1 = 10%, 0.2 = 20%.....

# sempre crie a variavel antes de usar
# tipos de variaveis
# tipo int - numeros inteiros
# tipo float - numeros com casa decimal
# tipo string - texto
# tipo boolean - verdadeiro ou falso

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("O faturamento foi de", faturamento  )
print("O custo foi de", custo )
print("o lucro foi de", lucro )
print("A margem foi de ", round (margem_lucro, 2) )
# round = ação para arredondar as casas decimais, definir o numero de casas decimais.


tempo_contrato = 170
tempo_anos = 170 / 12
print("Tempo em anos", int(tempo_anos))

# o sumbolo %, significa resto da divisão, ele atua como MOD (+, -, /, *)

tempo_meses = 170 % 12
print("Tempo em meses", tempo_meses)
