def generate_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes

def fibonacci(n, memo=None):
    """
    Generate the first n Fibonacci numbers using memoization.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if memo is None:
        memo = {}
    
    def fib(x):
        if x in memo:
            return memo[x]
        if x <= 0:
            return 0
        elif x == 1:
            return 1
        
        memo[x] = fib(x-1) + fib(x-2)
        return memo[x]
    
    return [fib(i) for i in range(n)]

if __name__ == "__main__":
    primes = generate_primes(100)
    print(f"First 100 prime numbers: {primes}")
    print(f"Total count of primes: {len(primes)}")
    
    fibs = fibonacci(10)
    print(f"\nFirst 10 Fibonacci numbers: {fibs}")
    print(f"Total count of Fibonacci numbers: {len(fibs)}")