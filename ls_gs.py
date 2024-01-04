a=10
"""def display():
    a=15
    def show():
     print(a)
    show()
display()
print(a)"""

"""a,b=4,5
if a<b:
   c=a+b
print(c)"""

#a=10
"""def display():
    a=20
    def show():
        global a
        a=25
    print(f"Value of a before calling show() function is {a}")
    show()
    print(f"Value of a after calling show() function is {a}")
display()
print(f"This is my global value {a}")"""

name='MalleswaraRao'
def display():
    global name
    name= name+" Chennu"
    print(name)
display()
print(name)




