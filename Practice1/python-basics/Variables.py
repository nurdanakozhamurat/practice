
x=5
y='hello'
print(x)
print(y)

x = 1       # x is of type int
x = "Nurr" # x is now of type str
print(x)

x = str(5)    # x will be '3'
y = int(5)    # y will be 3
z = float(5)  # z will be 3.0

x = 5
y = "Amir"
print(type(x))
print(type(y))

name='Alan'
age=15
print(name, end=" ")
print(age)

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "hard"
print(x, y, z)

x = "Python "
y = "is "
z = "hard"
print(x + y + z)


#Global Variables
x = "hard"

def myfunc():
  print("Python is " + x)

myfunc()


