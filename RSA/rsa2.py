import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2, x1 = x1, x
        d, y1 = y1, y
    
    if temp_phi == 1:
        return d + phi

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be the same.')
    n = p * q
    phi = (p-1) * (q-1)
    
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

# Example with Low Primes
p=174932539190556439133947949301046672067212836567814831037697709374159570332297048563930912989
q=188924649562447105873905191438096690373223263340438621507275879172605722507346531181064473053
public, private = generate_keypair(p, q)
message = "Hello"
encrypted_msg = encrypt(public, message)
decrypted_msg = decrypt(private, encrypted_msg)

print(f"Public Key: {public}")
print(f"Private Key: {private}")
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_msg}")
print(f"Decrypted Message: {decrypted_msg}")

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
