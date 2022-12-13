prod = float(input("Digite o valor do produto: R$"))
desc = float(input("Digite o valor do desconto: "))
valdesc = prod-(prod*desc/100)

print("Valor sem desconto: R$", prod)
print("Desconto :", desc, "%")
print("Valor com desconto: R$", valdesc)