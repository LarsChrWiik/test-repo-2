def generate_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    primes = generate_primes(100)
    print(f"First 100 prime numbers: {primes}")
    print(f"Total count: {len(primes)}")