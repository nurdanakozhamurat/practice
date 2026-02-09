#1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Nurdana", 18)

print(p1.name)
print(p1.age)


#2
class Person:
  pass

p1 = Person()
p1.name = "Nurdan"
p1.age = 18

print(p1.name)
print(p1.age)


#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Azalia", 15)

print(p1.name)
print(p1.age)


#4
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Nurdana")
p2 = Person("Alan", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


#5
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Nurdana", 18, "Almaty", "Kazakhstan")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
