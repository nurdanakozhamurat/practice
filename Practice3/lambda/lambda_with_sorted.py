#1
students = [("Alan", 9), ("John", 12), ("Jenny", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


#2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


#3
stuff_pin=[("Madina", 94), ("Aizhan", 96), ("Symbat", 88)]
sorted_stuff=sorted(stuff_pin, key=lambda x : x[1])
print(sorted_stuff)


#4
letters=["abcd", "ef", "g","hijk","lmnop"]
sorted_letters=sorted(letters, key=lambda x : len(x))
print(sorted_letters)


#5
numbers=[1,8,6,7,0,4,4]
sorted_numbers=sorted(numbers, key=lambda x : x)
print(sorted_numbers)