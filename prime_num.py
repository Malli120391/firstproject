import math
def prime_chceker(number):
    is_prime= True
    if is_prime==1:
        is_prime:False
    for i in range(2, math.ceil(number/2)+1):
        if number%1==0:
            is_prime=False
    if is_prime:
        print("It is a prime number")
    else:
        print("Not a prime number")
n= int(input("Enter a number:\n"))
prime_chceker(n)




