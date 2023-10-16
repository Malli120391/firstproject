"""var = "Welcome To TutorialsPoint"
print (type(var))"""

"""var = 'Welcome to "Python Tutorial" from TutorialsPoint'
print ("var:", var)

var = "Welcome to 'Python Tutorial' from TutorialsPoint"
print ("var:", var)"""

"""var = '''Welcome to TutorialsPoint'''
print ("var:", var)

var = "Welcome to TutorialsPoint"
print ("var:", var)"""

"""var = '''
Welcome To
Python Tutorial
from TutorialsPoint
'''
print ("var:", var)
"""

"""var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
print ("var[:5]:", var[:5])"""

"""var="HELLO PYTHON"
print ("var:",var)
print ("var[6:12]:", var[6:12])
print ("var[6:]:", var[6:])"""

"""var="HELLO PYTHON"
print ("var:",var)
print ("var[0:12]:", var[0:12])
print ("var[:]:", var[:])"""

"""s1="WORD"
print ("original string:", s1)
l1=list(s1)

l1.insert(3,"L")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)"""

"""import array as ar

s1="WORD"
print ("original string:", s1)

sar=ar.array('u', s1)
sar.insert(3,"L")
s1=sar.tounicode()

print ("Modified string:", s1)"""

"""mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"
count=0
for x in mystr:
   if x.lower() in vowels: count+=1
print ("Number of Vowels:", count)"""


mystr = '10101'

def strtoint(mystr):
   for x in mystr:
      if x not in '01': return "Error. String with non-binary characters"
   num = int(mystr, 2)
   return num
print ("binary:{} integer: {}".format(mystr,strtoint(mystr)))