"""PKCS#7 padding for block ciphers."""

def pkcs7_pad(data_hex, block_size=16):
    """Applies standard PKCS#7 padding to a hex data string."""
    data_bytes = bytes.fromhex(data_hex.replace(" ", ""))
    pad_len = block_size - (len(data_bytes) % block_size)
    padded = data_bytes + bytes([pad_len] * pad_len)
    return padded.hex().upper()


def pkcs7_unpad(padded_hex):
    """Strips PKCS#7 padding bytes and detects padding violations."""
    padded_bytes = bytes.fromhex(padded_hex.replace(" ", ""))
    pad_len = padded_bytes[-1]
    if pad_len < 1 or pad_len > len(padded_bytes):
        return "Error: Invalid padding threshold value."
    for b in padded_bytes[-pad_len:]:
        if b != pad_len:
            return "Error: Block padding verification mismatch!"
    return padded_bytes[:-pad_len].hex().upper()
