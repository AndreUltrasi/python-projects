#Fibonacci's Sequence
#1,1,2,3,5,8,13,21,34,55,89,144,233...
x=1
y=0
listf=[1]
while y<100:
    listf.append(x)
    x+=listf[y] 
    y+=1
    print(listf)