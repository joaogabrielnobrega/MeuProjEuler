def is_prime(x):
    for i in range(2, int(x** 0.5)+1):
        if x % i == 0:
            return False
    return True

n = 600851475143
factors = []
for a in range(2, int(n ** 0.5)+1):
    if n % a == 0:
        primo = is_prime(n / a)
        prima = is_prime(a)
        if prima:
            factors.append(a)
            if primo:
                factors.append(n / a)
print(factors)
