def multiply(x):
    tmp = x
    _sum = 0
    print(tmp)
    while tmp > 0:
        print(tmp)
        if tmp % 3 == 0:
            _sum += tmp
            tmp -= 1
            print(tmp)
        elif tmp % 5 == 0:
            _sum += tmp
            tmp -= 1
            print(tmp)
        else:
            tmp -= 1
    print(_sum)

   
multiply(999)       
