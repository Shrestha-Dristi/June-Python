
"""
WAP to sum all the digits of a three-digit number
input: 573
output: 15
"""


number = int(input("Enter a number"))
sum = 0
while number != 0:
    rem = number%10
    sum += rem
    number = number//10

print(sum)

number = input("Enter a number")
sum = 0

for each in number:
    sum += int(each)

print(sum)