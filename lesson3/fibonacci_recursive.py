def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Main Code
n = 10
print(f"Recursive method: Fibonacci({n}) = {fibonacci_recursive(n)}")
