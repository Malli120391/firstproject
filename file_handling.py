"""f1=open("file_1.txt", "w+")
print(f1.tell())
f1.write("Hey Python")
print(f1.tell())"""
#f1.write("Hi I am practicing python for data engineer")
#f1.write("  Hello")
#print(f1.read())
#f1.write("this is learning part ")
#data=f1.read()
#print(data)
"""print(f1.tell())
f1.write("Hello")
print(f1.tell())
print(f1.read())
print(f1.tell())"""
"""f1.write("This is my python code")
print(f1.tell())
f1.seek(0)
print(f1.tell())
data=f1.read()
print(data)
print(f1.tell())
f1.close()"""

"""f1=open("C:\Users\malle\Desktop\desktop_file.txt", "a+")
#f1=open("file_1.txt", "a+")
print(f1.tell())
f1.seek(0)
#f1.write(" Hello Code running")
print(f1.read())
f1.write(" Python running code")"""

f1=open("my_image1.jpg", "rb")
f2=open("my_image2.jpg", "wb")
for i in f1:
    f2.write(i)




