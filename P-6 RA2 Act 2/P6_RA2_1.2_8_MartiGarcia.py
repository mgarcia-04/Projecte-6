def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial(0):", factorial(0))
print("Factorial(3):", factorial(3))
print("Factorial(5):", factorial(5))