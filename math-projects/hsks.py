a =0
def aleatorio(x,y):
  from random import randint
  return randint(x,y) 

menor = 0
maior =0
cycle = 1
n =0
lista=[] 
while cycle < 400000:
  a = aleatorio(1,2)
  if a == 1:
    n +=1
    lista.append(n)
    if n > maior:
      maior = n
  if a == 2:
    n -=1
    lista.append(n)
    if n < menor:
      menor = n
  print(n) 
  cycle+=1
print("menor: ", menor) 
print("maior:", maior)
print("media: ", sum(lista)/len(lista)) 