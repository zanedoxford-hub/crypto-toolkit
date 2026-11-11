"""Worked examples that print step-by-step calculations."""
import cryptokit as ck

print("== Modular inverse (RSA private exponent) ==")
ck.extended_gcd_verbose(17, 3120)

print("\n== Square-and-multiply: 5^15 mod 23 ==")
ck.square_and_multiply_verbose(5, 15, 23)

print("\n== Textbook RSA ==")
k = ck.rsa_keygen(61, 53, 17)
c = ck.rsa_encrypt(65, k["e"], k["n"])
print(k, "ciphertext:", c, "decrypted:", ck.rsa_decrypt(c, k["d"], k["n"]))

print("\n== ElGamal ==")
p, g, x = 23, 5, 6
y = pow(g, x, p)
c1, c2 = ck.elgamal_encrypt(7, y, g, p, 3)
print("ciphertext:", (c1, c2), "decrypted:", ck.elgamal_decrypt(c1, c2, x, p))

print("\n== Elliptic curve y^2 = x^3 + 2x + 3 mod 97 ==")
P = (3, 6)
print("P =", P, " 2P =", ck.ec_point_double(P, 2, 97))

print("\n== Index of Coincidence ==")
print("English-like text IC:", round(ck.index_of_coincidence("it was the best of times it was the worst of times it was the age of wisdom " * 5), 4))
