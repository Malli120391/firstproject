"""list_1 = [1, 'a']
list_2 = range(2, 4)

list_joined = [*list_1, *list_2]
print(list_joined)"""

"""list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_joined = list(set(list_1 + list_2))
print(list_joined)"""

list1 = [1, 'a']
list2 = [1,2,3]

list2.extend(list1)
print(list2)