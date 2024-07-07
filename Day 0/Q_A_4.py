

# Write a python program to check whether the input number is prime or composite.
# 0 and 1 are neither prime nor composite.


# def prime_composite(num):
#     if num < 2:
#         return "Neither prime nor composite"
    
#     for i in range(2,num):
#         if num % i == 0:
#             return "Composite"
        
#     return "Prime"

# number = int(input("Enter a number"))
# result = prime_composite(number)
# print(result)

def prime_composite(num):
    if num <=1:
        return "Neither Prime nor Composite"
    
    else:
        count = 0
        count +=1 for i in range(num+1) if num % i == 0:
        if count == 2:
            return "Prime"

        else:
            return "Composite"


result = prime_composite()
print(result)
            