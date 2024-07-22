import json
filename = "students.json"


def update_student():
    id = input("Enter student id: ")
    key = input("Enter the info you want to update: ")
    value = input(f"Enter the new {key} ")

    if key not in ["name", "age", "address"]:
        print("Info not available")
    else:
        with open(filename, "r+") as fp:
            students = json.loads(fp.read())
            student = list(filter(lambda element:element["id"] == id, students))
            if student:
                student = student[0]
                student[key] = value
                