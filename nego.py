numero = int(input("digite um numero: "))
cont = 0
divisor = 1

while divisor <= numero:
    if numero%divisor==0:
            cont +=1
    divisor+=1
if cont ==2:
    print("o número é primo")
else:
    print(" o número não é primo")