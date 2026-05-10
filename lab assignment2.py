# Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Read input
n = int(input().strip())

# Print first n Fibonacci terms
for i in range(n):
    print(fibonacci(i), end=" ")
