"""def add(a,b):
    c=a+b
    print(f"Sum is {c}")
add(5,4)
add(9,10)"""

"""def great(name, dept):
    print(f"Hi {name}")
    print(f"Your from {dept} department")
great("MalleswaraRao", "Computer Science")"""

"""def great(name, dept):
    print(f"Hi {name}")
    print(f"Your from {dept} department")
great(dept="Computer Science", name="MalleswaraRao")"""

"""def great(name, dept):
    print(f"Hi {name}")
    print(f"Your from {dept} department")
great("MalleswaraRao", dept="Computer Science",)"""

"""def great(name, subject, dept="Computer Science"):
    print(f"Hey {name}")
    print(f"do you developing web application using {subject}")
    print(f"Your from {dept} department")
great("MalleswaraRao","Python")"""

"""def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"Sum is {c}")
add(5,5,5)
add(10,5,6)"""

"""def add(a, *numbers):
    c=0
    print(numbers)
    for i in numbers:
        c += i
    print(f"Sum is {c}")
add(1,2,5)
#add(10,5,6)
#add(1,2,3,4,56,8)"""

def info_person(*args, **kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
info_person(1,2,name="Malli", age=30, dept="Data Engineer")
info_person(1,2,3,name="Ram Nandan", dept="Future")