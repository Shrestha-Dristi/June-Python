

# Create a decorator function login_required which when applied to a function, asks for password.
# If the provided password is "1234" then excute the function else return "Invalid Password. User not authenticated"

def login_required(func):
    def inner_fxn(*args,**kwargs):
        pwd = input("Enter a password")
        if pwd == '1234':
        
            return func(*args,**kwargs)
        else:
            return"Invalid password"
    return inner_fxn


@login_required
def addition(a, b, c):
    return a + b + c


result = addition(1, 2, 3)
print(result)

