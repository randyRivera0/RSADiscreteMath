import time
import math
from rsa2 import mod_inverse, gcd

# Trial division for factorizing
def trial_division_factorize(n):
    factors = []
    # Check for smallest prime factor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append((i, n // i))
            return factors  # Return factors immediately when found
    
    # If no factor found, n is prime
    return [(n, 1)]

# Brute force method to find large primes (for demonstration purposes)
def find_large_primes():
    start = time.time()
    # Let's use larger primes
    #p = 32416190071
    p = 11
    #q = 32416190057
    q = 13
    large_public, large_private = generate_keypair(p, q)
    large_n = large_public[1]
    
    # Print the process of trying to brute force large primes
    print(f"Finding large primes for n = {large_n}...")
    for num in range(2, int(math.sqrt(large_n)) + 1):
        print(f"Trying {num}...")
        if large_n % num == 0:
            print(f"Succesful {num}...")
    
    end = time.time()
    print(f"Time taken: {end - start} seconds")

# Generate RSA key pairs
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# Example with Small Primes
small_p = 32416190071
small_q = 32416190057
small_public, small_private = generate_keypair(small_p, small_q)
small_n = small_public[1]

print(f"Small primes factorization (n = {small_n}):")
start_time = time.time()
small_factors = trial_division_factorize(small_n)
end_time = time.time()
print(f"Factors: {small_factors}")
print(f"Time taken: {end_time - start_time} seconds")

# Example with Large Primes
print("\n-----")
find_large_primes()
