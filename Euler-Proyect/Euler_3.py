import math 

def largest_prime_factor(n):
    # Si "n" es igual a 1, no tiene factor primo, así que retornamos 1.
    if n == 1:
        return 1
    
    # El bucle "while" comienza a probar los factores impares de "n", comenzando con el número 3.
    i = 3
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            # Si "n" es divisible por "i", actualizamos "n" al cociente de la división por "i".
            n //= i
        else:
            # Si "n" no es divisible por "i", aumentamos "i" en 2 y continuamos probando.
            i += 2
    
    # Si "n" es igual a 1, entonces "i" es el factor primo más grande de "n".
    if n == 1:
        return i
    # Si "n" es mayor que 1, entonces "n" es un factor primo y es el más grande.
    else:
        return n

# Llamamos a la función "largest_prime_factor" con el número 60.
print(largest_prime_factor(600851475143))

