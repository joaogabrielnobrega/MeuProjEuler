## Project euler
## Problema 9

a = 0
b = 1
c = 2
verify_pythagorian_sumAB = (a ** 2) + (b ** 2)
verify_pythagorian_c = (c ** 2)
sumABC = 0
nsum = 1
result = ""

while a < 500:
    while b < 600: 
        while c < 800:
            if a < b < c:
                if verify_pythagorian_sumAB == verify_pythagorian_c:
                    sumABC = a + b + c
                    if sumABC == 1000:
                        result = f"O resultado é A:{a} B:{b} C:{c}"
            if c % 200 == 0:
                print(f"Sum {sumABC}")
                print(f"a{a}  b{b}  c{c}")
            c += 1
            nsum = 1
            verify_pythagorian_sumAB = (a ** 2) + (b ** 2)
            verify_pythagorian_c = (c ** 2)
        b += 1
        c = 2
        nsum = 1
    a += 1
    b = 1
    c = 2
    nsum = 1

    

print(result)
