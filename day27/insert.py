from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student ID: ")
name = input("Enter student's name: ")
address = input("Enter student's address: ")
age = input("Enter student's age: ")

sql = f"""
INSERT INTO STUDENT (ID, NAME, ADDRESS, AGE) VALUES ('{id}','{name}','{address}',{age})
"""

cursor.execute(sql)
print("Student Added Successfully!!")
