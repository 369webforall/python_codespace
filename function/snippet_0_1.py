
# write a function to calculate 2 number, and return result

def calculator(n1, n2, symbol):
    if symbol == "+":
        return n1 + n2
    elif symbol == "-":
        if n1 > n2:
            return n1 - n2
        else:
            return n2 -  n1
    elif symbol == "*":
        return n1 * n2
    elif symbol == "/":
        return n1 / n2
    elif symbol == "%":
        print(n1 % n2) 
    

ans = calculator(5, 6 , "+")
print(ans)

calculator(4, 7, "%")

# Write a function `is_div_by_4` that accepts a number as an argument.
# The function should return a boolean indicating whether or not
# the number is divisible by 4.

def is_div_by_4(num):
    return num % 4 == 0

print(is_div_by_4(8))   # True
print(is_div_by_4(12))  # True
print(is_div_by_4(24))  # True
print(is_div_by_4(9))   # False
print(is_div_by_4(10))  # False

