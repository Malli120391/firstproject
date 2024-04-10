import my_module
a,b = 4,5
sum = a+b
print("Sum is: ", sum)
print("Value of a from another module is: ", my_module.a)

"""from my_module import *
print("Value of a from another module is : ", a)
print(area_of_square(3))
calculator(4,2)"""

"""from my_module import calculator,a,area_of_square
print(calculator(4,2))"""


"""import my_module as m
print(m.a)
print(m.area_of_square(4))"""

#import math
#print(math.e)

#print(help("modules"))
#print(help("random"))
#print(help("math"))