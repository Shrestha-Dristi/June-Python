# Using context manager we donot need to manually close a file

with open("example.txt", "r") as fp:
    data = fp.read()
    print(data)


with open("example.txt", "w") as fp:
    fp.write("Using context Manager")
print("Written to file")


with open("example.txt", "a") as fp:
    fp.write("\nThis is in new line")

with open("example.txt", "r+") as fp:
    data = fp.read()
    print(data)
    fp.seek(0)
    fp.write("New Data")

with open("example.txt", "w+") as fp:
    fp.write("Completely new data")
    fp.seek(0)
    data = fp.read()
    print(data, "<--------")