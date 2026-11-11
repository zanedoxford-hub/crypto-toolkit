"""Number theory helpers: GCD, extended Euclid, modular inverse and square-and-multiply."""

def gcd(a, b):
    """Returns the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd_raw(a, b):
    """Raw mathematical Extended GCD recursion."""
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd_raw(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y


def get_mod_inverse(a, m):
    """Returns the modular inverse 'x' where (a * x) % m == 1."""
    gcd_val, x, y = extended_gcd_raw(a, m)
    if gcd_val != 1:
        raise ValueError(f"Math Error: gcd({a}, {m}) is {gcd_val}, not 1. No inverse exists!")
    return x % m


def extended_gcd_verbose(a, b):
    """
    Executes the Extended Euclidean Algorithm and prints step-by-step equations
    showing exactly how to substitute the remainders by hand.
    Returns (gcd, x, y) such that (a * x) + (b * y) = gcd.
    """
    print(f"\n[Step-by-Step Extended GCD for Mod Inverse: gcd({a}, {b})]")
    steps = []
    original_b = b
    original_a = a
    
    # Forward Pass (Euclidean Algorithm)
    temp_a, temp_b = a, b
    while temp_b != 0:
        q = temp_a // temp_b
        r = temp_a % temp_b
        steps.append((temp_a, q, temp_b, r))
        print(f"  {temp_a} = ({q} * {temp_b}) + {r}")
        temp_a, temp_b = temp_b, r
        
    if temp_a != 1:
        print(f"  -> GCD is {temp_a}, not 1. No modular inverse exists!")
        return temp_a, 0, 0
        
    # Backward Pass (Substitution Workings)
    print("\n  [Backward Substitution Workings Isolation]")
    x, y = 0, 1
    last_x, last_y = 1, 0
    
    for i in range(len(steps) - 2, -1, -1):
        curr_a, q, curr_b, r = steps[i]
        if r == 1:
            print(f"  Isolate 1: 1 = {curr_a} - ({q} * {curr_b})")
            
    # Standard algebraic recurrence calculation
    gcd_val, x, y = extended_gcd_raw(a, b)
    print(f"  -> Final coefficients: ({a} * {x}) + ({original_b} * {y}) = {gcd_val}")
    return gcd_val, x, y


def square_and_multiply_verbose(base, exponent, modulus):
    """
    Executes modular exponentiation while printing an explicit execution matrix
    tracking the bits of the exponent from left to right.
    """
    if modulus == 1:
        return 0
    binary_exp = bin(exponent)[2:]
    print(f"\n[Square-and-Multiply Steps for {base}^{exponent} mod {modulus}]")
    print(f"  Exponent {exponent} in Binary: {binary_exp}")
    print(f"  {'Index':<6} | {'Bit':<4} | {'Operation Carried Out':<25} | {'Running Result'}")
    print(f"  {'-'*65}")
    
    result = 1
    for i, bit in enumerate(binary_exp):
        op_str = "Square"
        result = (result * result) % modulus
        if bit == '1':
            result = (result * base) % modulus
            op_str += " & Multiply"
        print(f"  {i+1:<6} | {bit:<4} | {op_str:<25} | {result}")
        
    print(f"  -> Final Modular Exponentiation Output = {result}")
    return result
