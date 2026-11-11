"""Diffie-Hellman key agreement over a prime field."""

def dh_public_value(g, private_secret, p):
    return pow(g, private_secret, p)


def dh_shared_secret(received_public, private_secret, p):
    return pow(received_public, private_secret, p)
