from estd_connection import estd_connection

cursor = estd_connection()

# cursor.execute("DROP TABLE STUDENT")

# In Python, we are using raw query to hit the SQL commands
# While using frameworks (Flask, Django, FastAPI) we do not enter raw SQL commands.
# Rather we use ORM (Object Relational Mapping)
# Popular ORM service for Python is SQLAlchemy

sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    ADDRESS CHAR(20),
    AGE INT
)
"""
cursor.execute(sql)
print("Table Created Successfully!")
