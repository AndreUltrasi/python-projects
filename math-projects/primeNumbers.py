def prime():
  x=int(input("Digite um número: "))
  if(x==1):
    print("Você digitou o número 1")
    prime()
  i=x-1
  while(True):
    if(i==1):
      print("É primo")
      break
    elif(x%i==0):
      print("Não é primo")
      print("{}%{} = {}".format(x,i,x%i))
      break
    elif(x%i!=0):
      i-=1
      
while(True):
  try:
    prime()
  except:
    print("Número inválido")