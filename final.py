print("Bem-vindo")

# Menú de opções
print("* * * * *  MENU  * * * * *")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Pares ou Ímpares")
print("6. Fatoriais")
print("7. Primo")

# Seleção do menu
select = int(input("Selecione uma opção (1-7): "))

if select == 1:
    v1 = int(input("Digite um número: "))
    v2 = int(input("Digite outro número: "))
    print("Resultado da soma:", v1 + v2)

elif select == 2:
    sub1 = int(input("Digite um número: "))
    sub2 = int(input("Digite outro número: "))
    print("Resultado da subtração:", sub1 - sub2)

elif select == 3:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print("Resultado da multiplicação:", num1 * num2)

elif select == 4:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if num2 != 0:
        print("Resultado da divisão:", num1 / num2)
    else:
        print("Não é possível dividir por zero!")

elif select == 5:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print(f"{num} é Par.")
    else:
        print(f"{num} é Ímpar.")

elif select == 6:
    import math
    num = int(input("Digite um número: "))
    if num < 0:
        print("Fatorial não existe para números negativos!")
    else:
        print("Fatorial de", num, "é:", math.factorial(num))

elif select == 7:
    num = int(input("Digite um número: "))
    if num < 2:
        print(f"{num} não é primo.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} não é primo.")
                break
        else:
            print(f"{num} é primo.")

else:
    print("Opção inválida. Tente novamente.")
