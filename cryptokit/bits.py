"""Bit-level helpers."""

def binary_xor(bin_str1, bin_str2):
    """Performs bitwise XOR logic gates on two matching binary strings."""
    b1 = bin_str1.replace(" ", "")
    b2 = bin_str2.replace(" ", "")
    if len(b1) != len(b2):
        return "Error: Binary strings length mismatch!"
    res = "".join("1" if x != y else "0" for x, y in zip(b1, b2))
    return " ".join([res[i:i+4] for i in range(0, len(res), 4)])


def lfsr_keystream(initial_state, taps, output_length):
    """
    Simulate a Fibonacci-style Linear Feedback Shift Register.

    initial_state: list of bits, e.g. [1, 0, 1, 0, 1]
    taps: indexes XORed together to form the feedback bit, e.g. [0, 4]
    Returns the first output_length output bits.
    """
    state = list(initial_state)
    keystream = []
    for _ in range(output_length):
        keystream.append(state[-1])
        feedback = 0
        for tap in taps:
            feedback ^= state[tap]
        state = [feedback] + state[:-1]
    return keystream
