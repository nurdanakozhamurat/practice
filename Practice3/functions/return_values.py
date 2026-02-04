#1
def my_function(x, y):
  return x + y

result = my_function(10, 6)
print(result)


#2
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#3
def my_function():
  return (4, 10)

x, y = my_function()
print("x:", x)
print("y:", y)


#4
def my_function(name, /):
  print("Hello", name)

my_function("Alan")


#5
def my_function(name):
  print("Hello", name)

my_function(name = "Alan")      #with ,/ you cant use keyword


#6
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")      #with *, you cant write without keyword


#7 Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)



