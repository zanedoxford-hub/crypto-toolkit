"""Classical ciphers, the Index of Coincidence statistic and Kasiski examination."""

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


def kasiski_examination(ciphertext, min_len=3, max_key_len=20):
    """
    Kasiski examination for guessing the key length of a Vigenere ciphertext.

    Finds every repeated sequence of at least min_len letters, records the
    distances between their occurrences, and counts how many of those
    distances each candidate key length (2..max_key_len) divides.
    The true key length (and its multiples) should divide most distances.

    Returns a dict:
      "repeats":    {sequence: [distances between consecutive occurrences]}
      "candidates": [(key_length, count), ...] sorted by count, highest first
    """
    clean = "".join(c for c in ciphertext.upper() if c.isalpha())
    positions = {}
    for i in range(len(clean) - min_len + 1):
        positions.setdefault(clean[i:i + min_len], []).append(i)

    repeats = {}
    for seq, pos in positions.items():
        if len(pos) > 1:
            repeats[seq] = [b - a for a, b in zip(pos, pos[1:])]

    distances = [d for ds in repeats.values() for d in ds]
    counts = {}
    for k in range(2, max_key_len + 1):
        hits = sum(1 for d in distances if d % k == 0)
        if hits:
            counts[k] = hits

    candidates = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return {"repeats": repeats, "candidates": candidates}
