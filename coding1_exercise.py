

weight = int(input("Enter weight in Kg: "))
height = int(input("Enter height in meter: "))

bmi = (weight/height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} and we are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are Obses.")
else:
    print(f"Your BMI is {bmi} and you are clinically Obses.")



