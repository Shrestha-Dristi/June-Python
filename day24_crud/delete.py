import json
filename = "students.json"


def delete_student():
    id = input("Enter the student id: ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
    student = list(filter(lambda element:element["id"] == id, students))
    if student:
        print(student[0])