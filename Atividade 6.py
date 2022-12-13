cpf1 = str(input("Qual seu CPF? "))
cpf2 = f"{cpf1[0:3]}.{cpf1[3:6]}.{cpf1[6:9]}-{cpf1[9:]}"
nome = str(input("Qual seu nome? "))
sobrenome = str(input("Qual seu sobrenome? "))
valor1 = 11677
valor2 = 15356
valor3 = valor1 + valor2

print("\nQuantidades de dígitos do cpf é: ", len(cpf1))
print("A última letra do nome é: ", nome[-1])
print("\nEu ", nome, " ", sobrenome, " do documento ", cpf2, " declaro \n"
    "que recebi no mês de novembro de 2022 a quantia de ", valor1, "\n"
    "na venda do Fiat Uno 99 e a quantia de ", valor2, " na venda\n"
    "da moto X1, somando a quanria de ", valor3, "\n")
