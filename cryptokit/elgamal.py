"""ElGamal encryption and signatures. For learning only."""

from .number_theory import gcd, get_mod_inverse

def elgamal_encrypt(M, y, g, p, k):
    """
    Encrypts integer message M using public key y, base g, prime p, and random k.
    Outputs the precise tuple coordinate system (C1, C2).
    """
    c1 = pow(g, k, p)
    c2 = (M * pow(y, k, p)) % p
    return c1, c2


def elgamal_decrypt(c1, c2, x, p):
    """Decrypts ciphertext block coordinates (C1, C2) using private exponent x."""
    mask = pow(c1, x, p)
    mask_inv = get_mod_inverse(mask, p)
    m_recovered = (c2 * mask_inv) % p
    return m_recovered


def elgamal_sign(m_hash, x, g, p, k):
    """Generates an ElGamal Digital Signature pair (r, s) modulo p-1."""
    if gcd(k, p - 1) != 1:
        raise ValueError(f"k={k} is not coprime to p-1={p-1}! Math cannot generate signature.")
    r = pow(g, k, p)
    k_inv = get_mod_inverse(k, p - 1)
    s = (k_inv * (m_hash - (x * r))) % (p - 1)
    return r, s


def elgamal_verify(m_hash, r, s, y, g, p):
    """Verifies validity of an ElGamal Signature coordinate string."""
    if not (0 < r < p):
        return False
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(g, m_hash, p)
    return v1 == v2
