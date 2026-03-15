#enumerate
students=["Madina", "Aizhan", "Nurdana"]
for i, name in enumerate(students):
    print(i, name)


#zip
names=["Madina", "Aizhan", "Nurdana"]
ages=[32, 30, 18]
for n,a in zip(names, ages):
    print(n, a)
