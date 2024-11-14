from encryption import encrypt_decrypt, cipher_to_txt, encrypt_decrypt_cipher
from key_guessing import find_key


def decrypt_and_save():
    with open('ciphers.txt', 'r') as file, open('decrypt_ciphers.txt', 'w') as result_file:
        # Read all lines from the file
        cipher_lines = file.readlines()

        # Iterate through the lines two by two (key-len, cipher)
        for i in range(0, len(cipher_lines), 2):
            # Read the key length and the cipher
            key_len = int(cipher_lines[i].strip())  # Convert key-len to integer
            cipher = list(map(int, cipher_lines[i + 1].strip().split(",")))  # Convert cipher to a list of integers

            # Guess the key using the key length
            guessed_key = find_key(cipher, key_len)

            # Decrypt the cipher using the guessed key
            decrypted_message = encrypt_decrypt_cipher(cipher, guessed_key)
            print(f"Guessed Key: {guessed_key}")
            print(f"Cracked Message:\n{decrypted_message}\n\n")
            # Write the result to decrypt_ciphers.txt
            result_file.write(f"Guessed Key: {guessed_key}\n")
            result_file.write(f"Decrypted Message: {''.join(map(str, decrypted_message))}\n\n")


if __name__ == '__main__':
    # Q1: Sample Text Encryption with Known Key
    plaintext = "This is a wonder world please make it safe"
    key = "abc"
    encrypted_txt = cipher_to_txt(encrypt_decrypt(plaintext, key))
    print(f"Encrypted Text: {encrypted_txt}\nLength: {len(encrypted_txt)}")
    # Q1: Sample Text Decryption with Known Key
    decrypted_txt = cipher_to_txt(encrypt_decrypt(encrypted_txt, key))
    print(f"Decrypted Text: {decrypted_txt}")

    # Q2: Sample Cipher Decryption with Known Key
    cipher = [10, 0, 8, 14, 10, 19, 13, 23, 8, 6]
    print(f"Decrypted Cipher: {encrypt_decrypt_cipher(cipher, key)}")

    # QB: Sample Cipher Decryption with Known Key-Length only! make sure provide key-len&cipher on ciphers.txt file
    decrypt_and_save()

