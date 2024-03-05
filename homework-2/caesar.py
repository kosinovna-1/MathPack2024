import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for c in plaintext:
        t = c
        if ord(c)>=ord('A') and ord(c)<=ord('Z'):
            t = chr(ord('A')+(ord(c)-ord('A')+shift)%26)
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            t = chr(ord('a')+(ord(c)-ord('a')+shift)%26)
        ciphertext += t
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = encrypt_caesar(ciphertext,-shift)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    for i in range(26):
        if decrypt_caesar(ciphertext.split()[0] in dictionary):
            return i
    return best_shift
