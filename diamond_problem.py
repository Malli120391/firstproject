class A:
    def dispaly(self):
        print("dispaly from A class")
class B(A):
    pass
    #def dispaly(self):
        #print("dispaly from B class")
class C(A):
    def show(self):
        print("Hello from C class")
    #def dispaly(self):
        #print("dispaly from B class")
class D(B,C):
    pass
    #def dispaly(self):
        #print("display from D class")
d1=D()
d1.dispaly()
print(D.mro())