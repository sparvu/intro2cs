def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Main code
n = 10
print(f"Iterative method: Fibonacci({n}) = {fibonacci_iterative(n)}")
