 
# Find the factorial of a given number iterative method
def factIteration(n):
    res = 1;
 
    # using iteration
    for i in range(1, n + 1):
        res *= i;
 
    return res;
 
num = 5;
print("Factorial(",num,") Iterative method:", factIteration(5));
