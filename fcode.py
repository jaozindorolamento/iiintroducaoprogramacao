altura = float(0)
qjogadores = int(input("digite a quantidade de jogadores"))
for i in range(qjogadores):
    altura = altura + float(input("digite a altura dos jogadores em metros"))

print(" a media de altura dos jogadores é:", (altura/qjogadores))