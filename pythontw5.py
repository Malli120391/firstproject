"""i = 0
while i<10:
    print("Python")
    i = i+2"""

i = 0
correctpassword = 'admin'
while i<10:
    pwd = input("Enter the password: ")
    if correctpassword == pwd:
        i=10
        break
    else:
        print("wrong password")
