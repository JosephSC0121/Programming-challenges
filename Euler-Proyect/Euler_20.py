# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
import numpy as np
def factorial(n):
    result = 1
    for i in range (1,n+1):
        result *= i
    return result

def sum_digits(num):
    return sum(np.array([int(n) for n in str(factorial(num))]))  
    
if __name__ == "__main__":
    print(sum_digits(100))
