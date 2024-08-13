import time
import math
from rsa2 import mod_inverse, gcd

# Trial division for small primes
def trial_division_factorize(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append((i, n // i))
            break
    return factors

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
small_p = 11
small_q = 13
small_public, small_private = generate_keypair(small_p, small_q)
small_n = small_public[1]

print(f"Small primes factorization (n = {small_n}):")
start_time = time.time()
small_factors = trial_division_factorize(small_n)
end_time = time.time()
print(f"Factors: {small_factors}")
print(f"Time taken: {end_time - start_time} seconds")

# Example with Large Primes
# Let's use larger primes
large_p = 32416190071
large_q = 32416190057
large_public, large_private = generate_keypair(large_p, large_q)
large_n = large_public[1]

print(f"\nLarge primes factorization (n = {large_n}):")
start_time = time.time()
large_factors = trial_division_factorize(large_n)
end_time = time.time()
print(f"Factors: {large_factors}")
print(f"Time taken: {end_time - start_time} seconds")

# Note: For a realistic large primes example (e.g., 2048-bit), GNFS would be needed
# and trial division would be infeasible. This is just an illustrative example.
