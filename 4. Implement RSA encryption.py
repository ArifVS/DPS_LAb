def power(base, expo, m):
    res = 1
    base = base % m
    for e in range(1,expo+1):
      res = (res*base)
    return res%m

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generateKeys():
    p = int(input("Enter your prime number: "))
    q = int(input("Enter your prime number: "))
    n = p * q
    phi = (p - 1) * (q - 1)

e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)

    return e, d, n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(m, e, n):
    return power(m, e, n)

def decrypt(c, d, n):
    return power(c, d, n)

if __name__ == "__main__":

    # Key Generation
    e, d, n = generateKeys()

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message
    M = int(input("Enter your numerical message: "))
    print(f"Original Message: {M}")

    # Encrypt the message
    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    # Decrypt the message
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")
