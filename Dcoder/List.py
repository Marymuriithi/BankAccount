print ("Hello, Dcoder!")
student= {'name':'ann','age':'20','year':'2000','country':'kenya','county':'Nairobi'}
print(student['name'])
print(student['age'])

eunice={'name':'Eunice','age':'12','year':'2008','country':'Kenya','county':'Nyeri'}
alice={'name':'Alice','age':'20','year':'2000','country':'Kenya','county':'Machakos'}
ann={'name':'Ann','age':'20','year':'2000','country':'Kenya','county':'Nakuru'}
agnes={'name':'Agnes','age':'22','year':'1998','country':'Kenya','county':'Mombasa'}
students=[eunice,alice,ann,agnes]
print(student)
for student in students:
  print(student['name'])
for student in students:
    name = student['name']
    age = student['age'] 
    county= student['county']
    sentence = "{} is {} years and is from {} county".format(name,age,county)
    print(sentence)
    
for student in students:
  print(student['age']*3)
  
  
for year in students:
  print(student['year'])