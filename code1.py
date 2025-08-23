
soma = 0
negativos = 0
for i in range(20):
    n = int(input())
    if n >0:
        soma += n
    elif n <0:
        negativos += 1

print("numeros positivos: ", soma)
print("numeros negativos: ", negativos)
