// not working
#Erdös Discrepancy Puzzle
#12 moves with 5 positions
real12 = [1,-1,-1,1,-1,1,1,-1,-1,1,1,-1]
real = [1,-1,-1,1,-1,1,1,-1,-1,1,1]
def check():
  for y in range(1,12):
    print (real)
    print (real[(y-1)::y])
    print ("sum = {}".format(sum(real[(y-1)::y])))
    print ("step = {}\n".format(y))
    
lista = [] 
i=1
while i<11:
  lista.append(1)
  if (-2<sum(lista[i-1::i])<2)==False:
    lista.pop()
    lista.append(-1)
    print(i) 
  i+=1
print(lista) 
    





"""
cracked = [] 
z=1
while z<12:
  cracked.append(1)
  if (sum(cracked)==2 or sum(cracked)==-2):
    cracked [-1] = -1
  z+=1
print(cracked) 
print(sum(cracked)) 
print(real) """
