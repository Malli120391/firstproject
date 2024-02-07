"""class Instructor:
    def __init__(self, ins_name, ins_address):
        self.name = ins_name
        self.address = ins_address
instructor_1 = Instructor("Malleswara Rao", "Hyderabad")
print(f"This is my Name {instructor_1.name} and address {instructor_1.address}")"""

class Instructor:
    followers=0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        #self.followers=0
    def display(self, subject_name):
        #print("Hi")
        print(f"Hi My Name is {self.name} and i learn {subject_name}")
    def update_followers(self, followers_name):
        self.followers += 1
instructor_1 = Instructor("Malleswara Rao", "Hyderabad")
print(instructor_1.name)
#print(instructor_1.display())
instructor_1.display("Python")
instructor_1.update_followers("Malli")
print(instructor_1.followers)
instructor_2 = Instructor("Malli", "Pune")
#print(instructor_2.followers)
instructor_2.update_followers("Om")
print(instructor_2.followers)