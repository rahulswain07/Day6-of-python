#Example of Dictionary
person={"name":"Rahul",
        "age":18,
        "course":"Computer science"}#name,age,course is keys and Rahul,18,computer science is value.
print(person)
#method of Dictionary example
#1.keys method
print(person.keys())
#2.values method
print(person.values())
#3.items method
print(person.items())
#4.get method
print(person.get('age'))
#5.update method
person.update({'age':21,'Email':"rahulgaming58708@gmail.com"})
print(person)
#6.pop method
person.pop("Email")
print(person)
#7.pop items method
person.popitem()
print(person)
#8.clear mmethod
person.clear()
print(person)
#9.copy method
person.copy()
print(person)
#10.loop
if "name" in person:
    print("exist your name")
else:
    print("youre name does not exist")