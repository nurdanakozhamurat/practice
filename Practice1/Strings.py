#1
a = "Hello"
print(a)

#2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#3
a = "Hello, World!"
print(a[0])

#4
txt = "She have been in Turkey"
print("Turkey" in txt)

#5
txt = "Hello, World!"
print(txt[1:6])

#Modify strings
a = "Nurdana!"
print(a.upper())

a = " Hello, World! "
print(a.strip())

a = "Good morning!"
print(a.replace("G", "J"))

a = "Hello, World!"
print(a.split(","))

#Concatinate strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#f-string
age = 18
txt = f"My name is Nurdana, I am {age}"
print(txt)

price = 85
txt = f"The price is {price:.2f} euros"
print(txt)