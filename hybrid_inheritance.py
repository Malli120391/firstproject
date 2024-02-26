class A:
    def dispaly(self):
        print("dispaly from A class")
class B(A):
    def dispaly(self):
        print("dispaly from B class")
class C:
    def show(self):
        print("Hello from C class")
class D(B,C):
    def dispaly(self):
        print("display from D class")
d1=D()
d1.dispaly()
print(D.mro())