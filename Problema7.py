#
#Project Euler
#   Problem 7

import datetime

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = datetime.datetime.now()

n = 1
primes = []
while len(primes) < 10001:
    n += 1
    if is_prime(n):
        primes.append(n)


print(primes[-1])

end = datetime.datetime.now()
print(end - start)