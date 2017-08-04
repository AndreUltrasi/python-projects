// verificação da equação do somatório
print("k1 = 1")
print("k1+ k2 +...+ m = (m*(m+1))/2")
k = 1
m=int(input("m = "))
tmp = k
print("k = ",k)
print("sum = ", tmp)
while k < m:
  k+=1
  tmp+=k
  print("k = ",k)
  print("sum = ", tmp)
print("sum [k1 = 1 to {}]  = ({}*({}+1))/2".format(m,m,m,m))
print("(m*(m+1))/2 = ",(m*(m+1))/2)
