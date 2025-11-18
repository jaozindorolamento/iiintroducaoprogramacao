print("Robô agrícola")

print("Informações: ")

bateria=int(input("Digite o Nível da bateria: "))

if bateria <20:
  print("Bateira muito Baixa! Retorne imediatamente para a base.")

if bateria >=20:
  if bateria <50:
    print("Atenção: Bateria em nível moderado.")
if bateria >50:
  print("Bateria suficiente para operação.")

print("Temperatura do ambiente ")
temp=float(input("Digite a temperatura: "))
if temp >40:
  print("Temperatura crítica! Operação suspensa.")
if temp >5:
   if temp <40:
      print("Temperatura Moderada.")
if temp <5:
  print("Frio extremo! Modo de economia ativado.")

print("Umidade do Solo: ")
umidade=int(input("Digite o nível da Umidade do solo: "))

if umidade <30:
  print("Solo muito seco. Recomendado iniciar irrigação")
if umidade >80:
  print("Solo encharcado! Suspenda irrigação imediatamente")

modo=input("Digite o Modo de operação: ")
col=("colheita")
pla=("plantio")
irri=("irrigação")

if modo==col:
  print("Iniciando modo COLHEITA...")
if modo ==pla:
  print("Iniciando modo PLANTIO...")
if modo==irri:
  print("Iniciando modo IRRIGAÇÃO...")


""" if bateria >=50:
  print("Robô autorizado a iniciar a operação.")
if not bateria >=50:
  print("Operação negada! Verifique as condições do ambiente.")
if temp >=10:
    print("Robô autorizado a iniciar a operação.")
if not temp >=10:
    print("Operação negada! Verifique as condições do ambiente.")

if temp <=35:
      print("Robô autorizado a iniciar a operação.")
if not temp <=35:
    print("Operação negada! Verifique as condições do ambiente.")
      
if umidade >=30:
    print("Robô autorizado a iniciar a operação.")

if not umidade <=80:
    print("Operação negada! Verifique as condições do ambiente.")
 """

if bateria >=50:
   if temp >=10:
      if temp <=35:
         if umidade >=30:
            if umidade <=80:
               print("Robô autorizado a iniciar a operação!")
            else:
               print("Operação negada! Verifique as condições do ambiente.")
         else:  
            print("Operação negada! Verifique as condições do ambiente.")
      else:
        print("Operação negada! Verifique as condições do ambiente")
   else:
        print("Operação negada! Verifique as condições do ambiente")    
else:
    print("Operação negada! Verifique as condições do ambiente")