#1
x = lambda a : a + 10
print(x(8))


#2
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))


#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(8)

print(mydoubler(4))


#4
x = lambda a, b : a * b
print(x(2, 6))


#5
def myfunc(n):
  return lambda a : a * n

x = myfunc(5)
y = myfunc(6)

print(x(2))
print(y(3))
