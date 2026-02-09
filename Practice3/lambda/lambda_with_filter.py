#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd = list(filter(lambda x: x % 2 != 0, numbers))
print(odd)


#2
numbers=[1,2,3,4,5,6,7,8,9]
even=list(map(lambda x : x % 2==0, numbers))
print(even)


#3
nums=[1,5,0,8,0,7,6,0,0]
zero=list(map(lambda x : x==0, nums))
print(zero)


#4
nums=[1,6,3,9,4,7,12]
div3=list(map(lambda x : x%3==0, nums))
print(div3)


#5
numbers=[1,2,3,4,5,6,7,8,9]
notdiv5=list(map(lambda x : x%5!=0, numbers))
print(notdiv5)