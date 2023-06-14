# Euler Project Problem #808
import math, time

def list_primality(n): # Criba de Erastótenes

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, len(is_prime), p):
                is_prime[i] = False
    return is_prime
    
def is_not_palindrome(x):
    if x == x[::-1]:
        return False
    return True

def compute(n, limit = 5*10**7):
    is_prime = list_primality(limit)
    primes = [i for (i, isprime) in enumerate(is_prime) if isprime]
    values = []
    for x in primes[5:]:
        num = str(pow(x, 2))
        if is_not_palindrome(num):
            reversed_num = int(num[::-1])
            sqrt_root = math.isqrt(reversed_num)
            if sqrt_root * sqrt_root == reversed_num:
                if is_prime[sqrt_root]:
                    values.append(int(num))
    return sum(values)
if __name__ == "__main__":
    start = time.time()
    print('Answer: ', compute(50))
    end = time.time()
    print('----',end-start,'-----')
