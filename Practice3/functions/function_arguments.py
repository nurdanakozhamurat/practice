#1
def my_function(name):
  print(name + " Refsnes")

my_function("Alan")
my_function("Bob")
my_function("Jeny")


#2
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Alan")    # "Alan" is an argument


#3
def my_function(surname, name):
  print(surname + " " + name)

my_function("Kozhamurat", "Nurdana")


#4
def my_function(name = "person"):
  print("Hello", name)

my_function("Arsen")
my_function("Dan")
my_function()
my_function("Sofia")


#5
def my_function(vechicle, name):
    print("She has a", vechicle)
    print("His", vechicle+"'s name is", name)

my_function( "car", "Lexus" )

