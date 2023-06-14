# Euler Project Problem 808
import math 
def sieve_of_eratosthenes(n):
    # Inicializar una lista de booleanos para marcar los números primos
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Marcar los múltiplos de los números primos encontrados
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Retornar una lista con los números primos encontrados
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

def reservible_primes():
    inverso = 0
    reversibles_primes = []
    n = 2500000
    primes = sieve_of_eratosthenes(n)
    for prime in primes:
        square = prime**2
        aux = str(square)
        if aux != aux[::-1]:
            num = int(aux[::-1])
            root = math.sqrt(num)
            if root in primes:
                print(square)
                reversibles_primes.append(square)
    return sum(reversibles_primes)

if __name__ == "__main__":
    print(reservible_primes())
