# Create a student dictionary. 
# Create a function which takes dictionary key (string) as argument and return the value of that key


student = {"name": "Alex", "age": 30, "address": "KTM"}

# def get_value():
    
#     key = input("Enter the key you want to access")  
#     if key == student.keys:
#         return student.values
#     else:
#         return "invalid key"
    


# result = get_value()
# print(result)


def get_value(x):
    r = student.get(x, "The info is not available")
    return r


key = input("Enter the key you want to access ")
result = get_value(key)
print(result)