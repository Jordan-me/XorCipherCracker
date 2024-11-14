def encrypt_decrypt(txt, key):
    key_len = len(key)
    segments = get_segments(txt, key_len)
    cipher = []
    for segment in segments:
        for i in range(len(segment)):
            cipher.append(ord(segment[i]) ^ ord(key[i % key_len]))
    return cipher


def encrypt_decrypt_cipher(cipher, key):
    result = [cipher[i] ^ ord(key[i % len(key)]) for i in range(len(cipher))]
    return cipher_to_txt(result)


def cipher_to_txt(cipher):
    return ''.join(chr(c) for c in cipher)


def get_segments(txt, key_len):
    return [txt[i:i + key_len] for i in range(0, len(txt), key_len)]
