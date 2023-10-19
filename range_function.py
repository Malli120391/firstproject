"""a=range(1,101)
for i in a:
 print(i)"""

"""total = 0
for i in range(1,101):
    total += i
print(total)"""

total = 0
for i in range(1,101):
    if i%2==0:
        total += i
print(total)