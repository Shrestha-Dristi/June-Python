# get()
# update()
# keys()
# values()
# items()
# pop()

student = {"name": "Jane", "age": 12, "address": "KTM"}
# roll = student["roll"]  # KeyError
# print(roll)  # 


# get()
roll = student.get("roll")
print(roll)  # None

name = student.get("name", "Ram")
print(name)  # Jane


# update()
student = {"name": "Jane", "age": 12, "address": "KTM"}
student.update(name="Jon")
print(student)

student.update({"age": 30, "roll": 3})
print(student)  # {"name": "Jon", "age": 30, "address": "KTM", "roll": 3}


# keys
student = {"name": "Jane", "age": 12, "address": "KTM"}
print(student.keys())  # dict_keys(["name", "age", "address"])
keys = student.keys()
print(keys) # dict_keys(["name", "age", "address"])
# k = keys[0]  # This raises error because this is not list/tuple/string


keys = list(student.keys())
print(keys)  # ["name", "age", "address"]

k = keys[0]
print(k)  # "name"


# values
student = {"name": "Jane", "age": 12, "address": "KTM"}
values = student.values()
print(values)  # dict_values(["Jane", 12, "KTM"])

values = list(values)
print(values)  # ["Jane", 12, "KTM"]


# items()
student = {"name": "Jane", "age": 12, "address": "KTM"}
items = student.items()
print(items)  # dict_items([('name', 'Jane'), ('age', 12), ('address', 'KTM')])

items = list(items)
print(items)  # [('name', 'Jane'), ('age', 12), ('address', 'KTM')]

address = items[2][1]
print(type(address))
print(address)


# pop()
vowels = ["a", "e", "i", "o", "u"]
data = vowels.pop(2)
print(data)  # "i"
print(vowels)  # ["a", "e", "o", "u"]

student = {"name": "Jane", "age": 12, "address": "KTM"}
data = student.pop("age")
print(data)  # 12
print(student)  # {"name": "Jane", "address": "KTM"}


students = {
    "student1":{"name": "Jon", "age": 30, "address": "KTM"},
    "student2":{"name": "Jane", "age": 30, "address": "BKT"},
    "student3":{"name": "Alex", "age": 21, "address": "LTP"},
    }

data = students.get("student3")
ata = data.pop("address")

print(students)

j = students.pop("student2")
x = j.pop("address")
print(x)
print(students)

students = [
    {"name": "Jon", "age": 30, "address": "KTM", "roll":3},
    {"name": "Jane", "age": 32, "address": "KTM", "roll":4},
    {"name": "Hary", "age": 12, "address": "BKT", "roll":5},
]


student = students.pop(1)
print(student) # {"name": "Jane", "age": 32, "address": "KTM"}
print(students)
"""
[
    {"name": "Jon", "age": 30, "address": "KTM", "roll":3},
    {"name": "Hary", "age": 12, "address": "BKT", "roll":5},
]
"""






