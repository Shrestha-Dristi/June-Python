



data = '121'

tada = data[::-1]

""" if data == tada:
    print("Palindrome")
else:
    print("Not Palindrome")
 """

number = 121
n = number
rev = 0
while number != 0:
    remain = number % 10  # 1  2  1
    rev = rev * 10 + remain  # 121
    number = number // 10  # 12  1  0

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")