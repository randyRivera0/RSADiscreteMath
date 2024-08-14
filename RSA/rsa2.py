import math


# Example with Low Primes
p=174932539190556439133947949301046672067212836567814831037697709374159570332297048563930912989
q=188924649562447105873905191438096690373223263340438621507275879172605722507346531181064473053


# Factorizing n
n = public[1]
print(f"n: {n}")
# factors = [(i, n//i) for i in range(2, int(math.sqrt(n)) + 1) if n % i == 0]
factors = []
for i in range(2, int(math.sqrt(n)) + 1):
    print(f"Trial factor: {i}")
    if n % i == 0:
        factors.append((i, n // i))

print(f"Factors of n: {factors}")

# Recovering Private Key
recovered_p, recovered_q = factors[0]
recovered_phi = (recovered_p - 1) * (recovered_q - 1)
recovered_d = mod_inverse(public[0], recovered_phi)
print(f"Recovered Private Key: ({recovered_d}, {n})")

# Decrypting with Recovered Private Key
recovered_private = (recovered_d, n)
recovered_decrypted_msg = decrypt(recovered_private, encrypted_msg)
print(f"Decrypted Message with Recovered Private Key: {recovered_decrypted_msg}")


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
