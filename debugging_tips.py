"""def display()
    for i in range(1,10):
        if i==10:
            print("Bye!")
display()"""

"""import random
dice_numbers=["One","Two","Three","Four","Five","Six"]
dice_num=random.randint(1,6)
print(dice_numbers[dice_num])"""

"""year=int(input("In which year you were born: "))
if year>1980 and year<=1996:
    print("you are a Millenial")
elif year>1996:
    print("You are a Gen Z")"""

"""age=int(input("How old are you: "))
print(type(age))
if age>=18:
    print(f"You can vote at {age}")"""

"""a,b=0,0
a=int(input("Enter a: "))
print(f"a is {a} ")
b==int(input("Enter b: "))
#b=int(input("Enter b: "))
print(f"b is {b} ")
multiplication=a*b
print(multiplication)"""

"""o=int(input("Enter your number: "))
if o%2 == 0:
    print("Even")
else:
    print("Odd")"""

for number in range(1,16):
    if number%3==0 or number%5==0:
        print("FizzBuzz")
    if number%3==0:
        print("Fizz")
    if number%5==0:
        print("Buzz")
    else:
        print(number)

