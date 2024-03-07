Salary  =int(input("Enter the Salary "))
Expenses  =int(input("Enter the Expenses "))
Saving = Salary - Expenses
Percentage = (Saving/Salary) *100

if Percentage > 20:
  print("Good Saving")
else:
  print("No Saving")