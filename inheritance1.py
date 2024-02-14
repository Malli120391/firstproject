class Human:
    def __init__(self, num_heart):
        self.num_eys=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")
    """def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")"""
    def display(self):
        print(f"Hi, i am {self.name} and I have {self.num_heart} heart.")
male_1=Male("Malli",1)
#male_1.work()
#male_1.flirt()
print(male_1.num_eys)
print(male_1.name)
#print(male_1.num_heart)
male_1.display()
