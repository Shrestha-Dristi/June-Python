#WAP to check whether an input is odd or even

num = int(input("Enter a number"))

if num % 2 == 1:
    print("(num) is odd")

else:
    print("(num) is odd")


#WAP to three numbers input and print the greatest number

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

if all([a > b, a > c]):
    print("(a) is the greatest")
elif all([b > a, b > c]):
    print("(b) is the greatest")
else:
    print("(c) is the greatest")