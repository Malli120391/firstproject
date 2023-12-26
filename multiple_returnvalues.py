"""import statistics

def mean_median_mode(list1):
    #return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)

#print(mean_median_mode([3, 5, 45, 3, 21, 89]))
a,b,c=mean_median_mode([3, 5, 45, 3, 21, 89])
print(f"Mean is {a}\nMedian is {b}\nMode is {c}")"""

def add(a,b):
    if a==0 & b==0:
        return "You have entered zero for both values"
    else:
        return a+b
var1=int(input("Enter First Value:\n"))
var2=int(input("Enter Second Value:\n"))
result=add(var1,var2)
print(result)
