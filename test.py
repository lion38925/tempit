# inheritance and classes
'''
print("Hello World")

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname,classroom):
        Person.__init__(self,fname,lname)
        self.classroom = classroom
    
    def printclass(self):
        print(self.classroom)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
y= Student("gamer","coder","1")
y.printclass()
y.printname()

'''
#list
'''
fruits = ['orange','apple','guava','mango']
for i in fruits:
    print(i)


myi=iter(fruits)
#print(next(myi))
print(" ")
fruits.append('pineapple')

for i in fruits:
    print(i)
print(" ")
fruits.pop()
for i in fruits:
    print(i)

'''
# try and exception
'''
try:
  print(x)
except:
  print("An exception occurred")

'''

# dictionary
'''
car= {
    "model":"x11",
    "colour": "red"

}


for x,y in car.items():
    print(x,y)

'''

# matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()
'''
'''
import numpy as np
for i in range(10):
  if not i % 2 == 0:
    print(i+1)

'''
'''
a=input("enter please")
print(a)
'''
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
  
  def show(self,name,age):
    print(self.name)

p1 = Person("John", 36)
Person.show('a',6)
'''
l=['1','2','3']
print(l[:1])
k="keys"
print(k[:1])