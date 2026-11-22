# cryptokit: Step-by-Step Cryptography in Python

[![Tests](https://github.com/zanedoxford-hub/crypto-toolkit/actions/workflows/tests.yml/badge.svg)](https://github.com/zanedoxford-hub/crypto-toolkit/actions/workflows/tests.yml)

A small Python toolkit that implements classic and public-key cryptography primitives **and shows the working**, the way you would on paper. I built it while studying Cryptography (3012ICT) at Griffith University and then cleaned it up into a tested package.

> **For learning only.** These are textbook implementations (no padding schemes, no constant-time code, tiny parameters). Never use them to protect real data. Use a vetted library such as `cryptography` or `libsodium`.

## What's inside

| Module | Functions |
|---|---|
| `number_theory` | GCD, extended Euclidean algorithm (with printed working), modular inverse, square-and-multiply (with a bit-by-bit table) |
| `classical` | Caesar and Vigenère ciphers, Index of Coincidence (to tell mono- from poly-alphabetic ciphers) |
| `bits` | Binary XOR, LFSR keystream generator |
| `padding` | PKCS#7 pad / unpad with validation |
| `rsa` | Key generation, encrypt / decrypt, sign / verify |
| `diffie_hellman` | Public values and shared secret |
| `elgamal` | Encrypt / decrypt, sign / verify |
| `ecc` | Elliptic curve point addition and doubling over a prime field |

## Quick start

```bash
git clone https://github.com/zanedoxford-hub/crypto-toolkit.git
cd crypto-toolkit
python examples.py        # prints worked examples
pip install pytest
python -m pytest -q       # 10 tests
```

```python
import cryptokit as ck

ck.square_and_multiply_verbose(5, 15, 23)
# Exponent 15 in Binary: 1111
# Index  | Bit  | Operation Carried Out     | Running Result
# 1      | 1    | Square & Multiply         | 5
# ...

keys = ck.rsa_keygen(61, 53, 17)       # {'n': 3233, 'phi': 3120, 'e': 17, 'd': 2753}
c = ck.rsa_encrypt(65, keys["e"], keys["n"])
ck.rsa_decrypt(c, keys["d"], keys["n"])  # 65
```

## How I used it

- **Breaking classical ciphers:** the Index of Coincidence (English is about 0.066, random text about 0.038) separated a Vigenère ciphertext from a simple substitution one. Combined with Kasiski examination, it revealed the key length.
- **Stream ciphers:** the LFSR simulator generated and checked keystreams by hand-verifiable steps.
- **Public-key maths:** the verbose functions show every step of modular inverses and exponentiation, which makes it easy to check RSA, Diffie-Hellman and ElGamal calculations.

## What I learned

- Why textbook RSA and ElGamal are insecure without padding and randomness.
- Why ECB mode leaks patterns and CBC does not.
- How edge cases (no modular inverse, the point at infinity, invalid padding) break naive implementations, so each one has a test.

## Author

Zane Doxford, Bachelor of Cyber Security student, Griffith University (Gold Coast).
[Portfolio](https://zanedoxford-hub.github.io) · [LinkedIn](https://www.linkedin.com/in/zane-doxford-9a80022ba/)
