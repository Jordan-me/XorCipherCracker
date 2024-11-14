from collections import Counter

from encryption import encrypt_decrypt_cipher
from score_english import score_decrypted_text


def get_histo(data):
    diction = Counter(data)
    return dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))


def transpose_data_blocks(data_blocks):
    return [[data_blocks[j][i] for j in range(len(data_blocks))] for i in range(len(data_blocks[0]))]


def get_xor_mat_ascii():
    ascii_start = 32
    ascii_end = 126
    xor_matrix = {}
    for row in range(ascii_start, ascii_end + 1):
        xor_matrix[chr(row)] = {chr(col): row ^ col for col in range(row, ascii_end + 1)}
    return xor_matrix


def find_xor_positions(value, xor_matrix):
    return [(row_char, col_char) for row_char, xor_row in xor_matrix.items() for col_char, xor_value in xor_row.items()
            if xor_value == value]


def get_most_prob_key(keys_candidates, data):
    max_score = -1
    most_prob_key = ""
    for key in keys_candidates:
        score = score_decrypted_text(encrypt_decrypt_cipher(data, key))
        if score > max_score:
            max_score = score
            most_prob_key = key
    return most_prob_key


def get_histo_indices(data_mat):
    return [get_histo(row) for row in data_mat]
