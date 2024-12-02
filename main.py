def generate_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == "__main__":
    primes = generate_primes(100)
    print(f"First 100 prime numbers: {primes}")
    print(f"Total count of primes: {len(primes)}")
    
    fibs = fibonacci(10)
    print(f"\nFirst 10 Fibonacci numbers: {fibs}")
    print(f"Total count of Fibonacci numbers: {len(fibs)}")