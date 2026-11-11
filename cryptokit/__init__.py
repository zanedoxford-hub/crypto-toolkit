"""cryptokit: step-by-step implementations of classic and public-key cryptography primitives for learning."""

from .number_theory import gcd, extended_gcd_raw, get_mod_inverse, extended_gcd_verbose, square_and_multiply_verbose
from .classical import caesar_cipher, vigenere_cipher, index_of_coincidence
from .bits import binary_xor, lfsr_keystream
from .padding import pkcs7_pad, pkcs7_unpad
from .rsa import rsa_keygen, rsa_encrypt, rsa_decrypt, rsa_sign, rsa_verify
from .diffie_hellman import dh_public_value, dh_shared_secret
from .elgamal import elgamal_encrypt, elgamal_decrypt, elgamal_sign, elgamal_verify
from .ecc import ec_point_add, ec_point_double
