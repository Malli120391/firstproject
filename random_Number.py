import random

"""random_number = random.randint(0,10)
print("Random Numbers between 0 and 10:", random_number)"""

start_range = 1
end_range = 10
num_number = 5

random_numbers = random.sample(range(start_range, end_range+1), num_number)

print("Random numbers without repeate", random_numbers)