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
