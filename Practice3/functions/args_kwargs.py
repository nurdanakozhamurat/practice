#1
def my_function(*people):
  print("The youngest child is " + people[2])

my_function("Azalia", "Amir", "Alan")


#2
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Azalia", "Amir", "Alan")


#3
def my_function(word, *names):
  for name in names:
    print(word, name)

my_function("Hello", "Emil", "Tobias", "Linus")


#4
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 5))
print(my_function(1, 20, 15, 4))
print(my_function(6))


#5
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


#1
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Nurdana", lname = "Kozhamurat")


#2
def my_function(**var):
  print("Type:", type(var))
  print("Name:", var["name"])
  print("Age:", var["age"])
  print("All data:", var)

my_function(name = "Nurdana", age = 18, city = "KZO")


#3
def my_function(username, **info):
  print("Username:", username)
  print("Additional informations:")
  for key, value in info.items():
    print(" ", key + ":", value)

my_function("nurdana007", age = 18, city = "Almaty", hobby = "dance")


#4
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Nurdana", "Kozhamurat", age = 19, city = "Almaty")


#5
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)


#6
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Nurdana", "lname": "Kozhamurat"}
my_function(**person)