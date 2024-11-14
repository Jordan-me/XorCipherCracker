def create_bigram_counts(data, key_len):
    bigram_counts = {}
    for i in range(len(data) - 1):
        bigram = (data[i], data[i + 1])
        mod_position = i % key_len
        if bigram not in bigram_counts:
            bigram_counts[bigram] = [0] * key_len + [0]
        bigram_counts[bigram][mod_position] += 1
        bigram_counts[bigram][-1] += 1
    return bigram_counts
