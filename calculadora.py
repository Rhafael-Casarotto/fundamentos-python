# Projeto para fixar os conhecimentos
print("Vamos calcular?")
num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")
num1 = float(num1)
num2 = float(num2)


print("Escolha a operação: ")
print("1 = Soma")
print("2 = Subtração")
print("3 = Divisão")
print("4 = Multiplicação")

operacao = input("Digite aqui: ")

if operacao == "1":
    resultado = num1 + num2
    print("O resultado é: ", resultado)
elif operacao == "2":
    resultado = num1 - num2 
    print("O resultado é: ", resultado)   
elif operacao == "3":
    if num2 == 0:
        print("Não é possivel efetuar a divisão.")
    else:
        resultado = num1 / num2
        print("O resultado é: ", resultado)    
elif operacao == "4":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
else:
    print("Volte sempre") 




      