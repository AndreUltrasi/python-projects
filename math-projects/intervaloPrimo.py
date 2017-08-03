def primo(x):
  i=x-1
  while(True):
    if(i==1):
      print(x,end=" ")
      break
    elif(x%i==0):
      break
    elif(x%i!=0):
      i-=1
while(True):
  try:
    inicio=int(input("Início do Intervalo: "))
    if (inicio<2):
      inicio=2
    fim=int(input("Fim do Intervalo: "))
    while(inicio<=fim):
      primo(inicio)
      if(inicio==(fim-1)):
      	  print("")
      inicio+=1
  except:
    print("Número inválido")
  
  