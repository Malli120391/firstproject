import random

name=input("Enter every one's name separated by comma:")
names_list=name.split(",")
#print(names_list)
#length=len(names_list)
#random_choice= random.randint(0, length-1)
#person_selected=random.choice(names_list)
print(f"{random.choice(names_list)} will pay the bill")