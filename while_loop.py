"""count = 1
while count<=5:
    print(count)
    count += 1
print("out from loop")"""

"""count = 5
while count>0:print(count);count -= 1
print("out from loop")"""

"""count = 5
while count>0:
    print(count)
    count -= 1
    if count == 3:
        break
else:
    print("in else block")
print("out from loop")"""

"""number = int(input("enter a number (-1 to quit)"))
while number != -1:
    print(number)
    number = int(input("enter a number (-1 to quit)"))
else:
    print("in else block")
print("out from loop")"""

"""count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
else:
    print("out else block")
print("out from loop")"""

total = 0
number = int(input("enter a number(0 to quit):"))
while number !=0:
    total = total+number
    number = int(input("enter a number(0 to quit):"))
print("total is",total)





