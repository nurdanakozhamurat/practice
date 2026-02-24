#1
import math
degree=float(input("Enter degree: "))
radian=degree*math.pi/180
print("Radian: ",radian)



#2
import math
h=float(input())
base1=float(input())
base2=float(input())

area=(base1+base2)*h/2
print("Area of the trap: ",area)



#3
import math
n=int(input())
s=float(input())
area=(n*s*s)/(4*math.tan(math.pi/n))
print("Area of the pol: ",area)



#4
base=float(input())
h=float(input())
area=base*h
print("Area of the par: ",area)

