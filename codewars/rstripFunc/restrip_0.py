def no_boring_zeros(n):
    if n == 0:
        return 0
    else:
        num1 = str(n)
        num1 = num1.rstrip("0")
        return int(num1)


#---------------another method---------------

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip("0"))
    except ValueError:
        print("Invalid input")

try:
    user_input = int(input("Enter your input: \n"))
    print(no_boring_zeros(user_input))
except Exception as e:
    print("Invalid input")
