#opreatio of sets
s1={1,10,2,20,3,30,4,40}#union
s2={40,50,60,7,}
print(s1.union(s2))
print(s1.intersection(s2))#intersection
print(s1.difference(s2))#A-B
print(s1^s2)#in a or b not both symetric differencej
print(s1.issubset(s2))#false
print(s1.issuperset(s2))#false
print(s1.isdisjoint(s2))#false,no commen element return true