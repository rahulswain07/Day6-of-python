#beginer level practice
#Q1.Create a dictionay your own information
info={'name':'Rahul',
      'age':18,
      'course':'computer science',
        'contact':8260595178,}
print(info)
#Q2.Add mobile number to dictionar
info.update({'mb':7752068957})
print(info)
#Q3.update your age 21.
info.update({'age':21})
print(info)
#Q4.Remove your course from the dictionary
info.pop('course')
print(info)
#Q5.print all keys 
print(info.keys())
#Q6.print all values
print(info.values())
#Q7.check if "email"key exist or not
if 'Email' in info:
    print('your Email is exist your own info')
else:
    print('your email Doesnt exist')
#Q8.Add a new key email with a value 
info.update({'Email':"Rahulgaming58708@gmail.com"})
print(info)
#internedate practice Question
#Q1.create a dictionary using two lists:
keys=['name','age']
value=['Rahul',18]
person=dict(zip(keys,value))
print(person)
#create adictionry of 5 subjects marks
marks={'odia':90,
       'English':80,
       'math':70,
       'physics':50,
       'chemistry':50}
print(marks)
#Q2.calcate total and  average marks
total=sum(marks.values())
num_subject=len(marks)
average=total/num_subject
print(average)
#Q3.Create a dictionary where keys arenumbers from 1 to 5 and values are square
square_values={1:1*1,
               2:2*2,
               3:3*3,
               4:4*4,
               5:5*5}
print(square_values)
#Q4.merge two dictionary
dict1={'name':'rahul','age':18}
dict2={'dist':'kendrapara'}
dict1.update(dict2)
print(dict1)
#Q5. reverse a dictionary
student = {
    "name": "Rahul",
    "course": "BCA"
}
reversed_dict ={value:key for key, value in student.items()}
