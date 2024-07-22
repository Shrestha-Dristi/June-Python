# Enumerate is used to count the for loop in python

vowels = ("a", "e", "i", "o", "u")
result = enumerate(vowels)
print(result)
print(list(result))


result = enumerate(vowels, start=1)
print(list(result))

result = enumerate(vowels, start=5)
print(list(result))  

data = [6,2,1,9,40,12,21,100]

#with enumrate:
result = []
num = enumerate(data)
for key, value in num:
    if value % 2 == 0:
        result.append(key)
print(list(result))    #[0,1,4,5,7]

#without enumerate

result = []
for i in data:
    if i % 2 == 0:
        i_index = data.index(i)
        result.append(i_index)

print(list(result)) 


 