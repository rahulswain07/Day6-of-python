set={10,20,30,40}
set.add(50)
print(set)
set.remove(20)
print(set)
if 30 in set:
    print("if 30 is exist your set")
else:
    print('30 can not exist your set')
#l=[1,2,2,3,4,4,5]
#my_set=set(l)
#print(my_set)
set1={1,2,3,}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
a={1,2}
b={1,2,3,4}
if a.issubset(b):
    print("a is a subset")
else:
    print('a dont sub set b')
if a.issuperset(b):
    print('a is a superset b')
else:
    print('a dont superset b')
square={x**2 for x in range(1,6)}
print(square)
b.clear()
print(b)
str1 = "apple"
str2 = "grape"

# Convert strings to sets of characters
set1 = set(str1)
set2 = set(str2)

# Find intersection (common letters)
common_letters = set1 & set2

print("Common letters:", common_letters)
