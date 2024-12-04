import math 
def factorial(n):
    if (n>=0):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
    return "the number in negative"

print(factorial(5))
print(math.factorial(5))