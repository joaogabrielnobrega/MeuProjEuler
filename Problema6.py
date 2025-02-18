#
#Project Euler 
#    problema 6
#
import datetime

start = datetime.datetime.now()

def sumSquare(n):
    soma = 0
    for i in range(1, n + 1):
        soma += (i ** 2)
    return soma

def squareSum(n):
    square = sum(range(1, n + 1)) ** 2
    return square

num = 100
a = sumSquare(num)
b = squareSum(num)
print(a, "Sum square")
print(b, "Square sum")
print(b - a, "Diference")

end = datetime.datetime.now()
print(end - start)