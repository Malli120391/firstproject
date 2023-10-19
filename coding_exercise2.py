numbers = input("Enter your list of numbers: ")
# 34 45 12 -8 89 67
numbers_list = numbers.split()
count = 0
for number in numbers_list:
    count += 1
print(f"The length of list is: {count}")
#for i in range(0, len(numbers_list)):
for i in range(0,count):
    numbers_list[i] = int(numbers_list[i])
max_number = numbers_list[0]
for number in numbers_list:
    if number > max_number:
        max_number=number
print(f"The maximum number of is : {max_number}")
#print(numbers_list)


