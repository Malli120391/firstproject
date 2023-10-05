
set1 = {'Malli', 'Kalyani', 'NewBaby'}
set2 = {'NewBaby', 'Jathin', 'Aadi'}
set3 = {'Amarnadh', 'Raju', 'Malli'}
#print(set1.union(set2))
#print(set1.union(('Mohan', 'NewBaby')))
#print(set1 | set2 | set3)
#print(set1 |('Mohan', 'NewBaby'))
#set1.update(set2)
#print(set1)
#set1 |= set2
#print(set1)
#print(set1.intersection(set2,set3))
#print(set1.intersection(['Mohan', 'NagaRaju']))
#print(set1 & set2 & set3)
#set1.intersection_update(set2)
#print(set1)
#print(set1.difference(set2))
#print(set1 - set2)
#print(set1.difference(('Mohan', 'NagaRaju')))
#print(set1.difference(set2,set3))
#print(set1.symmetric_difference(set2, set3))
#print(set1 ^ set2 ^ set3)
#set2.symmetric_difference_update(set1)
#print(set2)
set1.symmetric_difference_update(('Mohan', 'NagaRaju'))
print(set1)
print(set2)
