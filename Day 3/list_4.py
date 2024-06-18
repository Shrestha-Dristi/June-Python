# List is a mutable datatype in Python
# List is a sequence of heterogenous data separated by comma and enclosed within big brackets

# Creating non-empty list
a = [1, 2]
b = ["a", "e", "i", "o"]
v = [1, 2, "a", "Hello", [1, 2], {1, 2}, 2.2]

# Creating empty lists
x = []
print(x)
y = list()


# Accessing elements of list
# List elements can be accessed using indexing and slicing

# indexing
vowels = ["a", "e", "i", "o", "u"]

print(vowels[4])    #u
print(vowels[0])    #a
print(vowels[2])    #i
#print(vowels[10])   #index error

print(vowels[-1])   #u
print(vowels[-4])   #e
#print(vowels[-10])  #index error


# slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(data[2:8]) #cdefgh  
print(data[:7]) #abcdefg
print(data[0:9])    # abcdefghij
print(data[6:])     #ghij
print(data[7:3])    #""
print(data[-8:-3])  #cdefg
print(data[-4: -2]) #gh
print(data[2:-3])   #cdefg
print(data[-9:9])   #bcdefghi
print(data[2:9:2])  #cegi

# slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(data[2:8])  # [c..."h"]
print(data[:7])  # ["a", "b", "c", "d", "e", "f", "g"]
print(data[0:9]) # ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(data[6:])  # ["g", "h", "i", "j"]
print(data[7:3])  # []
print(data[-8:-3])  # ["c", "d", "e", "f", "g"]
print(data[-4: -2])  # ["g", "h"]
print(data[2:-3])  # ["c", "d", "e", "f", "g"]
print(data[-9:9])  # ["b", "c", "d", "e", "f", "g", "h", "i"]
print(data[2:9:2])  # ["c", "e", "g", "i"]