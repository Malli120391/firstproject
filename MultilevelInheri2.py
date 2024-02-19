class Human:
    can_breath=True
    def __init__(self,num_heart):
        print("Calling from init Human class")
        self.eyes=2
        self.heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self, name):
        print("Calling init from Male class")
        self.name=name
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    def __init__(self,heart,name,can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.known_dancing=can_dance
    def work(self):
        #Human.work(self)
        super().work()
        print("I can code")
class Programming(Boy):
    def work(self):
        print("I can write programs")
boy_1=Boy(1,"Om Namah Shivaya", True)
print(boy_1.name)
print(boy_1.known_dancing)
print(boy_1.can_breath)
#boy_1.eat()
#boy_1.work()
#pro_1=Programming()
#pro_1.work()
print(Boy.mro())