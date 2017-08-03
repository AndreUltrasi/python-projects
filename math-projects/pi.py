#Real
#1.6449340668482264
#by python when m = 10**6
#1.6449330668487701
pi=3.14159265358979323846264338327950288419716939937510582097494459230781
m = 300000
#1/(k**4)=(pi**2)/6
k=int(input("k: "))
tmp=1/k**2
print("k = ",k)
print("soma = ", tmp)
while k <= m:
  print("k = ",k)
  print("soma = ", tmp)
  k+=1
  tmp+=1/k**2
print("(pi**2)/6 = ", pi**2/6) 
