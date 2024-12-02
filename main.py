def generate_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes

def generate_fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

if __name__ == "__main__":
    # Generate and print prime numbers
    primes = generate_primes(100)
    print(f"First 100 prime numbers: {primes}")
    print(f"Total count of primes: {len(primes)}")
    
    # Generate and print Fibonacci numbers
    fibonacci = generate_fibonacci(100)
    print(f"\nFirst 100 Fibonacci numbers: {fibonacci}")
    print(f"Total count of Fibonacci numbers: {len(fibonacci)}")