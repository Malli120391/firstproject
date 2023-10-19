for python in range(1,16):
    if python%3==0 and python%5==0:
        print("FizzBuzz")
    elif python%3==0:
        print("Fizz")
    elif python%5==0:
        print("Buzz")
    else:
        print(python)