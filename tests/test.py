from xor_encryption_decryption.encryption import encrypt_decrypt, encrypt_decrypt_cipher
from xor_encryption_decryption.key_guessing import find_key

test_text_1 = "All happy families are alike; each unhappy family is unhappy in its own way. Everything was in " \
              "confusion in the house of the Oblonskys. The wife had discovered that the husband was unfaithful to " \
              "her, and she had told him that she could no longer live with him. The husband had tried to justify " \
              "himself by pleading his love for his wife, but she would not listen to him. In the midst of all this " \
              "turmoil, the Oblonskys' children, servants, and guests were caught up in the emotional whirlwind. They " \
              "could not understand the cause of the unrest, but they could feel the tension in the air. The tension " \
              "was so thick that even the air seemed to crackle with it. The family was broken, and there seemed to " \
              "be no way to repair the damage. "
test_text_2 = "Call me Ishmael. Some years ago--never mind how long precisely--having little or no money in my purse, " \
              "and nothing particular to interest me on shore, I thought I would sail about a little and see the " \
              "watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. " \
              "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my " \
              "soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear " \
              "of every funeral I meet; and especially whenever my hypos get such an upper hand of me, " \
              "that it requires a strong moral principle to prevent me from deliberately stepping into the street, " \
              "and methodically knocking people's hats off--then, I account it high time to get to sea as soon as I " \
              "can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon " \
              "his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, " \
              "almost all men in their degree, some time or other, cherish very nearly the same feelings towards the " \
              "ocean with me. "
keys = ["hello", "python7",  "abc", "analysis", "test", "secure", "mysterykey"]

ciphers_test_1 = []
ciphers_test_2 = []
for key in keys:
    ciphers_test_1.append(encrypt_decrypt(test_text_1, key))
    ciphers_test_2.append(encrypt_decrypt(test_text_2, key))

# decrypt tests
for i in range(len(ciphers_test_2)):
    cipher = ciphers_test_2[i]
    key_len = len(keys[i])
    guessed_key = find_key(cipher, key_len)
    res = encrypt_decrypt_cipher(cipher, guessed_key)
    print(f"decrypted_txt =\n{res}\n\n")
    if guessed_key == keys[i]:
        print(f"test pass! text = test_text_1, key = {guessed_key}")

for i in range(len(ciphers_test_1)):
    cipher = ciphers_test_1[i]
    key_len = len(keys[i])
    guessed_key = find_key(cipher, key_len)
    res = encrypt_decrypt_cipher(cipher, guessed_key)
    print(f"decrypted_txt =\n{res}\n\n")
    if guessed_key == keys[i]:
        print(f"test pass! text = test_text_1, key = {guessed_key}")
