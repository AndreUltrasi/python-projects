#1=1/2+1/4+1/8....
x=0
y=1
while y!=56:
  x+=1/(2**y)
  print ("y =",y)
  print(x)
  y+=1