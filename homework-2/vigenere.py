def encrypt_vigenere(plaintext: str, keyword: str) -> str:

    def shift(i):
        step = i%len(keyword)
        symb = keyword[step]
        if ord(symb)>=ord('A') and ord(symb)<=ord('Z'):
            return ord(symb)-ord('A')
        if ord(symb)>=ord('a') and ord(symb)<=ord('z'):
            return ord(symb)-ord('a')
        return 0
    
    ciphertext = ""
    i = 0
    for c in plaintext:
        t = c
        if ord(c)>=ord('A') and ord(c)<=ord('Z'):
            t = chr(ord('A')+(ord(c)-ord('A')+shift(i))%26)
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            t = chr(ord('a')+(ord(c)-ord('a')+shift(i))%26)
        ciphertext += t
        i += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    def invers():
        dekey = ''
        for c in keyword:
            t = c
            if ord(c)>ord('A') and ord(c)<=ord('Z'):
                t = chr(ord('A')+ord('Z')+1-ord(c))
            if ord(c)>ord('a') and ord(c)<=ord('z'):
                t = chr(ord('a')+ord('z')+1-ord(c))
            dekey += t
        return dekey
        
    plaintext = encrypt_vigenere(ciphertext, invers())
    return plaintext
