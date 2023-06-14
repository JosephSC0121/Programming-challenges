import time, math

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]
	
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    return list(set(factors))

def phi(n):
    total = n
    prime_factor = prime_factors(n)
    
    for p in prime_factor:
        total *= (1-1/p)
        
    return (total)

def maxprimefactors(limit):
    total = 1
    primes = list_primes(int(math.sqrt(limit)))
    for i in primes:
        if total * i > limit:
            break
        else:
            total *= i
    return total

if __name__ == "__main__":
    while True:
      userinput = input("Please input an integer: ")
      start_time = time.time()
      temp = maxprimefactors(int(userinput))
      print(temp)
    print("--- %s seconds ---" % (time.time() - start_time))
