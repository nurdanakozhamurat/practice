#1
import re

s=input("1: ")
res=re.match(r'ab*', s)
print(res)


#2
import re

s=input("2: ")
res=re.match(r'^ab{2,3}$', s)
print(res)


#3
import re

s=input("3: ")
res=re.findall(r'[a-z]+_[a-z]+', s)
print(res)


#4
import re

s=input("4: ")
res=re.findall(r'[A-Z][a-z]+', s)
print(res)


#5
import re

s=input("5: ")
res=re.search(r'a.*b', s)
print(res)


#6
import re

s=input("6: ")
res=re.sub(r'[,.]', ":", s)
print(res)


#7
def snake_to_camel(s):
    part=s.split("_")
    return part[0]+"".join(i.capitalize() for i in part[1:])

s=input("7: ")
print(snake_to_camel(s))


#8
import re

s=input("8: ")
res=re.findall(r'[A-Z][a-z]*', s)
print(res)


#9
import re

s=input("9: ")
res=re.sub(r'[A-Z]', r' /1', s).strip()
print(res)


#10
import re

s=input("10: ")
res=re.sub(r'([A-Z])', r'_/1', s).lower()
print(res)
