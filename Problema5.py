# Smallest Multiple of [1 to 20]

last_number = 20
primes = []

for i in range(2, last_number + 1):
    prime = True
    for div in range(2, int(i**0.5) + 1):
        if i % div == 0:
            prime = False
            break
    if prime:
        primes.append(i)

factors = {prime: 1 for prime in primes}

for x in range(1, last_number + 1):
    factorsx = {prime: 0 for prime in primes}
    for i in primes:
        while x % i == 0:
            factorsx[i] += 1
            x /= i
    for prime, times in factorsx.items():
        factors[prime] = max(times, factors[prime])

result = 1
for prime, times in factors.items():
    result *= (prime ** times)

print(f"Smallest number divisible for 1 to 20{result}")
