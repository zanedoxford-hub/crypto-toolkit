"""Classical ciphers and the Index of Coincidence statistic."""

def caesar_cipher(text, shift, mode="encrypt"):
    """Encrypts or decrypts a string using a numeric Caesar shift (A=0, Z=25)."""
    out = []
    s = shift if mode == "encrypt" else -shift
    for char in text.upper():
        if char.isalpha():
            val = ord(char) - ord('A')
            out.append(chr(((val + s) % 26) + ord('A')))
        else:
            out.append(char)
    return "".join(out)


def vigenere_cipher(text, key, mode="encrypt"):
    """Processes string text using a polyalphabetic Vigenere repeating key."""
    out = []
    key = key.upper()
    key_idx = 0
    for char in text.upper():
        if char.isalpha():
            p_val = ord(char) - ord('A')
            k_val = ord(key[key_idx % len(key)]) - ord('A')
            shift = k_val if mode == "encrypt" else -k_val
            out.append(chr(((p_val + shift) % 26) + ord('A')))
            key_idx += 1
        else:
            out.append(char)
    return "".join(out)


def index_of_coincidence(text):
    """Calculates the Index of Coincidence (IC) to discover mono vs poly text."""
    clean = [c for c in text.upper() if c.isalpha()]
    n = len(clean)
    if n <= 1:
        return 0.0
    freqs = {}
    for c in clean:
        freqs[c] = freqs.get(c, 0) + 1
    sum_f = sum(f * (f - 1) for f in freqs.values())
    return sum_f / (n * (n - 1))
