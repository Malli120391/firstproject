farTemp = float(input("Enter the temperature in fahranheit: "))
#(farTemp - 32) * 5/9

celTemp = (farTemp-32)*5/9
print(celTemp)

if celTemp >= 30:
    print("Hot")
else:
    print("Cool")

