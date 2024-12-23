## Project euler
## Problema 39

a = 0
b = 1
c = 2
verify_pythagorian_sumAB = (a ** 2) + (b ** 2)
verify_pythagorian_c = (c ** 2)
p = 0
result = ""


while p <= 1000:
    while a < 500:
        while b < 600: 
            while c < 800:
                if a < b < c:
                    if verify_pythagorian_sumAB == verify_pythagorian_c:
                        p = a + b + c
                        result = result + str(p)
                        
                        print(f"p {p}")
                        print(f"a{a}  b{b}  c{c}")
                c += 1
                verify_pythagorian_sumAB = (a ** 2) + (b ** 2)
                verify_pythagorian_c = (c ** 2)
            b += 1
            c = 2
        a += 1
        b = 1
        c = 2

    

print(result)

