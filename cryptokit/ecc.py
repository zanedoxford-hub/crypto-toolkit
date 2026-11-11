"""Elliptic curve point arithmetic over y^2 = x^3 + ax + b mod p."""

from .number_theory import get_mod_inverse

def ec_point_add(P, Q, a, p):
    """Adds two points P=(x1, y1) and Q=(x2, y2) over y^2 = x^3 + ax + b mod p."""
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P[0] % p, P[1] % p
    x2, y2 = Q[0] % p, Q[1] % p
    
    if x1 == x2 and (y1 + y2) % p == 0:
        return None # Point at Infinity
        
    if x1 != x2:
        # Standard Point Addition Slope
        num = (y2 - y1) % p
        den = (x2 - x1) % p
        lam = (num * get_mod_inverse(den, p)) % p
    else:
        # Special Case: Point Doubling (P == Q)
        if y1 == 0:
            return None # Vertical tangent line maps to infinity
        num = (3 * pow(x1, 2, p) + a) % p
        den = (2 * y1) % p
        lam = (num * get_mod_inverse(den, p)) % p
        
    x3 = (pow(lam, 2, p) - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)


def ec_point_double(P, a, p):
    """Wrapper mapping point doubling configuration."""
    return ec_point_add(P, P, a, p)
