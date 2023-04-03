import math

def prime_numbers(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# IDENTIDAD DE CASSINI

def is_fibonacci(n):
    # Check if the input value is valid
    if n <= 0:
        return False
    # Check if the number is a perfect square
    root1 = math.isqrt(5*n*n + 4)
    root2 = math.isqrt(5*n*n - 4)
    if root1**2 == 5*n*n + 4 or root2**2 == 5*n*n - 4:
        return True
    else:
        return False
    
def is_even(n):
    if n % 2 == 0:
        return True
    return False

if __name__ == "__main__":
    n = int(input("Type a number: "))
    
if prime_numbers(n):
    print(f"{n} prime number,", end=' ')
else:
    print(f"{n} not prime number,", end=' ')
    
if is_fibonacci(n):
    print("fibonacci,", end=' ')
else:
    print("not fibonacci,", end=' ')

if is_even(n):
    print("even.")
else:
    print("odd.")
