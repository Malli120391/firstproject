
height = int(input("What is Your Height? "))
bill = 0
if height>=3:
    print("Can ride")
    age = int(input("What is Your age? "))
    if age<12:
        bill = 150
        print("Ticket Price is 150 Rs. ")
    elif age<=18:
        bill = 250
        print("Ticket Price 250 Rs. ")
    else:
        bill = 500
        print("Ticket Price 500 Rs. ")

        want_photo = input("do you want take photo(Y/N)")
        if want_photo == 'y' or want_photo == 'Y':
            bill = bill + 50
        print(f"Your total bill is {bill}")
else:
    print("Can't ride!")
    print("Bye")