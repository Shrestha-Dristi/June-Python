import csv
filename = "day28/students.csv"

# with open(filename, "r") as cr:
#     data = csv.DictReader(cr)
#     for each in data:
#         print(each)

# print(result)


with open(filename, "r") as cr:
    data = csv.DictReader(cr)
    result = [each for each in data]
    # result = []
    # for each in data:
    #     result.append(each)

print(result)

