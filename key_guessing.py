from functools import reduce
from utils import get_histo, get_xor_mat_ascii, find_xor_positions, get_most_prob_key, transpose_data_blocks, \
    get_histo_indecies


def guess_keys(histogram_indices, key_chars_candidates):
    most_common_chars_long_text = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r']
    keys = [""]
    for i, histogram in enumerate(histogram_indices):
        max_occur = max(histogram, key=histogram.get)
        new_keys = []
        for common_char in most_common_chars_long_text:
            xor_result_key = chr(ord(common_char) ^ max_occur)
            if xor_result_key in key_chars_candidates[i]:
                for existing_key in keys:
                    new_keys.append(existing_key + xor_result_key)
        keys = new_keys
    return keys

def find_key(data, key_len):
    data_blocks = [data[i * key_len:(i + 1) * key_len] for i in range(len(data) // key_len)]
    if len(data) % key_len != 0:
        last_row = data[len(data) // key_len * key_len:]
        last_row += [-1] * (key_len - len(last_row))
        data_blocks.append(last_row)
    transposed_data_blocks = transpose_data_blocks(data_blocks)
    histo_indices = get_histo_indecies(transposed_data_blocks)
    mat_xor_ascii = get_xor_mat_ascii()
    key_chars_candidates = []

    for row in transposed_data_blocks:
        row_options = {el: find_xor_positions(el, mat_xor_ascii) for el in set(row) if el > 0}
        intersection = reduce(lambda x, y: x & y, (set(char for pair in opts for char in pair) for opts in row_options.values()))
        key_chars_candidates.append(intersection)

    guessed_keys = guess_keys(histo_indices, key_chars_candidates)
    return get_most_prob_key(guessed_keys, data)
