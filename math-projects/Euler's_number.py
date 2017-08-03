#1/0!+1/1!+1/2!+1/3!+1/4!+1/5!+1/6!...
#Real Euler's number
#e=2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178...
#by Python
#e=2.7182818284590455
def factorial(z):
    elist=[]
    product=1
    while z>0:
        elist.append(z)
        z-=1
    for z in elist: 
        product *= z
    return product


z=0
list=[]
while z!=19:
    x=1/factorial(z)
    list.append(x)
    z+=1
    print("e = ",sum(list))
    print(z)
