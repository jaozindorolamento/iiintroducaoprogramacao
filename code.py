somaValor = 0
contnegativo = 0
for i in range(20):
    valor=int(input("digite um valor"))
    if valor >=0:
        somaValor +=valor
    else: contnegativo += valor

else:
    contnegativo+=valor

print("a soma dos valores positivos é", somaValor)
print("a soma dos valores negativos é", contnegativo)