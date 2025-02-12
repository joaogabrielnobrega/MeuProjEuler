fibonacci = [1, 2]
soma = 0

while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
if fibonacci[-1] > 4000000: del fibonacci[-1]
print(fibonacci)

for n in fibonacci:
    if n % 2 ==0:
        soma += n

print(soma)