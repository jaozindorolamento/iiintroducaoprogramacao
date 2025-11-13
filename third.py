usuario = "admin"
senha = "1234"
login = input("Usuário")
pwd = input("Senha")
if login == usuario:
    if pwd==senha:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta")

else:
    print("usuario inexistente")
