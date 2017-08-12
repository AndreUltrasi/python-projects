"""Problem 7￼
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?
"""
def prime_position(x):
    prime_ord = 0
    prime = 2
    tmp = prime - 1
    prime_list = []
    while prime_ord < x:
        while True:
            if tmp == 1:
                prime_ord += 1
                prime_list.append(prime)
                print("ordinal, prime", prime_ord, prime)
                break
            elif prime % tmp == 0:
                break
            elif prime % tmp != 0:
                tmp -= 1
        prime += 1
        tmp = prime - 1
    print(prime_list, x)

x = int(input("Digite a ordinalidade do numero primo: "))
prime_position(x)


