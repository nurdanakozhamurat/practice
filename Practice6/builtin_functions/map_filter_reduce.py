from functools import reduce

nums=[1,2,3,4,5]

#example map
squ=list(map(lambda x: x*x, nums))
print("Map:", squ)


#example filter
even=list(filter(lambda x: x%2==0, nums))
print("Filter:", even)


#example reduce
r=reduce(lambda a,b: a+b, nums)
print("Reduce:", r)