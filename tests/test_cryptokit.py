import pytest
import cryptokit as ck


def test_gcd_and_inverse():
    assert ck.gcd(48, 18) == 6
    assert ck.get_mod_inverse(5, 108) == 65
    assert (5 * 65) % 108 == 1
    with pytest.raises(ValueError):
        ck.get_mod_inverse(6, 9)


def test_square_and_multiply_matches_pow(capsys):
    assert ck.square_and_multiply_verbose(5, 15, 23) == pow(5, 15, 23)


def test_caesar_and_vigenere_round_trip():
    msg = "ATTACK AT DAWN"
    assert ck.caesar_cipher(ck.caesar_cipher(msg, 3), 3, "decrypt") == msg
    assert ck.vigenere_cipher("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
    assert ck.vigenere_cipher("LXFOPVEFRNHR", "LEMON", "decrypt") == "ATTACKATDAWN"


def test_index_of_coincidence_english_vs_random():
    english = "it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness " * 10
    assert ck.index_of_coincidence(english) > 0.05
    assert ck.index_of_coincidence("abcdefghijklmnopqrstuvwxyz" * 10) < 0.045


def test_kasiski_examination_finds_key_length():
    plain = "it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness " * 3
    cipher = ck.vigenere_cipher(plain, "LEMON")
    result = ck.kasiski_examination(cipher)
    assert result["repeats"]
    assert all(d % 5 == 0 for ds in result["repeats"].values() for d in ds)
    assert result["candidates"][0][0] == 5
    assert ck.kasiski_examination("ABCDEFGHIJ")["candidates"] == []


def test_xor_and_lfsr():
    assert ck.binary_xor("1010", "0110") == "1100"
    assert ck.lfsr_keystream([1, 0, 0], [0, 2], 7) == [0, 0, 1, 1, 1, 0, 1]


def test_pkcs7_round_trip():
    padded = ck.pkcs7_pad("AABBCC", 8)
    assert padded == "AABBCC0505050505"
    assert ck.pkcs7_unpad(padded) == "AABBCC"
    assert ck.pkcs7_unpad("AABBCC0505050504").startswith("Error")


def test_rsa_encrypt_decrypt_sign_verify():
    k = ck.rsa_keygen(61, 53, 17)
    assert k["n"] == 3233 and k["d"] == 2753
    c = ck.rsa_encrypt(65, k["e"], k["n"])
    assert ck.rsa_decrypt(c, k["d"], k["n"]) == 65
    s = ck.rsa_sign(123, k["d"], k["n"])
    assert ck.rsa_verify(s, k["e"], k["n"]) == 123


def test_diffie_hellman_shared_secret():
    p, g, a, b = 23, 5, 6, 15
    A, B = ck.dh_public_value(g, a, p), ck.dh_public_value(g, b, p)
    assert ck.dh_shared_secret(B, a, p) == ck.dh_shared_secret(A, b, p)


def test_elgamal_encrypt_decrypt_and_signature():
    p, g, x = 23, 5, 6
    y = pow(g, x, p)
    c1, c2 = ck.elgamal_encrypt(7, y, g, p, 3)
    assert ck.elgamal_decrypt(c1, c2, x, p) == 7
    r, s = ck.elgamal_sign(10, x, g, p, 5)
    assert ck.elgamal_verify(10, r, s, y, g, p)
    assert not ck.elgamal_verify(11, r, s, y, g, p)


def test_ecc_points_stay_on_curve():
    a, b, p = 2, 3, 97
    on_curve = lambda P: (P[1] ** 2 - (P[0] ** 3 + a * P[0] + b)) % p == 0
    P = (3, 6)
    assert on_curve(P)
    P2 = ck.ec_point_double(P, a, p)
    P3 = ck.ec_point_add(P2, P, a, p)
    assert on_curve(P2) and on_curve(P3)
    assert ck.ec_point_add(P, (P[0], -P[1] % p), a, p) is None
