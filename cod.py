print("Bem-vindo")

i = input(print("press Enter"))


print("* * * * *  MENU  * * * * *")
print("         Escreva           ")
print("1 para soma ")
print("2 para subtração ")
print("3 para multiplicação ")
print("4 para divisão ")
print("5 para pares ou impares ")
print("6 para fatoriais ")
print("7 para primo ")
print("8 para Sair")
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
select = int(input(print("selecione:")))

if select ==a:

    v3 = 0
    v1 = int(input(print("digite um número")))
    v2 =int(input(print("digite outro número")))

    v3 +=v1+v2


    print(v3)


if select ==b:
    niga = 0
    sub1 = int(input(print("digite um número")))
    sub2 = int(input(print("digite outro número")))

    niga+=sub1+sub2


    print(niga)




if select ==c:
    mult = 0
    num1 = int(input(print("digite um número")))
    num2 = int(input(print("digite outro número")))

    mult+=num1*num2


    print(num1, "*", num2, "=",mult)

if select ==d:

    num11 = float(input(print("digite um número")))
    num22 = float(input(print("digite outro número")))
    div = 0

    div += num11/num22

    print("O resultado da operação é: ",div)

if select == e:
    nn1 = int(input(print("digite um número")))
    nn2 = int(input(print("digite outro número")))

    if nn1/2==0  and nn1/nn1:
        print(" o numero",nn1, " é par")

    else: 
        print(" o numero", nn1, "é impar")

    if nn2/3==0:
        print(" o numero",nn2, " é impar")
        
    else:
        print(" o numero", nn2, "é par")


#print("6 para fatoriais ")
if select ==f:
    numero1 = int(input("digite um número"))
    numero2 = int(input("digite outro número"))

    fatorial1 = 1
    fatorial2 = 1

    for i in range(1, numero1 + 1):
        fatorial1 *= i

    for i in range(1, numero2 + 1):
        fatorial2 *= i

    print("o fatorial de ", numero1, "é :", fatorial1)
    print("o fatorial de ", numero2, "é :",fatorial2)



if select ==g:
    if select == 7:
     num = int(input("Digite um número: "))
    
    if num < 2:
        print("o",num, "não é primo.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("o",num, "não é primo.")
                break
        else:
            print("o",num, " é primo.")


    
    
    num0 = int(input("Digite outro número: "))
    if num0 < 2:
        print("o",num0, "não é primo.")
    else:
        for l in range(2, num0):
            if num0 % l == 0:
                print("o",num0, "não é primo.")
                break
        else:
            print("o",num0, " é primo.")


if select ==h:
    print("Saindo, até mais....")



