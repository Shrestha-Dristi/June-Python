
"""Create student with keys id, name, age, .
Take a input from the user, which (id, name, age or department) he wants to access and print .
Handle the possible exceptions."""

student = {"id":1, "name":"Ramram", "age": 500, "department": "IT"}

try:

    info = input("What info would you like to access?:")
    print(f"The {info} of the student is {student[info]}")

except KeyError:
    print("Enter a valid key")