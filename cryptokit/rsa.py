"""Textbook RSA (no padding). For learning only."""

from .number_theory import gcd, get_mod_inverse

def rsa_keygen(p, q, e):
    """Derives standard RSA keys including modulus n and totient phi."""
    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError(f"e={e} and phi={phi} share factors! GCD is {gcd(e, phi)}.")
    d = get_mod_inverse(e, phi)
    return {"n": n, "phi": phi, "e": e, "d": d}


def rsa_encrypt(M, e, n):
    return pow(M, e, n)


def rsa_decrypt(C, d, n):
    return pow(C, d, n)


def rsa_sign(M_hash, d, n):
    return pow(M_hash, d, n)


def rsa_verify(S, e, n):
    return pow(S, e, n)
