print("Resultado final do ano letivo.")
nota1 = input("Digite a nota do 1° trimestre: ")
nota2 = input("Digite a nota do 2° trimestre: ")
nota3 = input("Digite a nota do 3° trimestre: ")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

media = (nota1 + nota2 + nota3) / 3
print(f"A média é: {media:.2f}")

if media >= 7:
    print("Aprovado")
    print("Parabens, bom trabalho!")
elif media >= 5:
    print("Recuperação")
    print("Ainda da tempo, vamos lá!")
else:
    print("Reprovado")
    print("Não desista.")
  





   






