"""11-2=3**2
1111-22=33**2
111111-222=333**2"""
n = 1
while n != 18 :
  tmp = n
  x = 0
  y = 0
  while tmp > 0:
    x += 10**(tmp-1)*(10**(tmp-1) + 10**(tmp))
    tmp -= 1
  tmp = n
  while tmp > 0:
    y += 2*10**(tmp-1)
    tmp -= 1
  z = int((x - y)**0.5)
  print ("n =",n)
  print("{} - {} = {}**2".format(x,y,z))
  n += 1

