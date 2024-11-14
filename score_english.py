from consts import common_english_words, common_english_bigrams, common_english_trigrams, common_english_quadrigrams, \
    most_common_english_letters_primary, most_common_english_letters_secondary


def count_occurrences(target_text, substring):
    # Counts occurrences of a substring within a larger string
    return target_text.count(substring)


def score_decrypted_text(deciphered_text):
    common_word_matches = 0
    common_bigram_matches = 0
    common_trigram_matches = 0
    common_quadrigram_matches = 0
    common_letter_matches = 0

    # Count occurrences of common English words
    for word in common_english_words:
        common_word_matches += count_occurrences(deciphered_text, word)

    # Count occurrences of common English bigrams
    for bigram in common_english_bigrams:
        common_bigram_matches += count_occurrences(deciphered_text, bigram)

    # Count occurrences of common English trigrams
    # for trigram in common_english_trigrams:
    #     common_trigram_matches += count_occurrences(deciphered_text, trigram)

    # Count occurrences of common English quadrigrams
    # for quadrigram in common_english_quadrigrams:
    #     common_quadrigram_matches += count_occurrences(deciphered_text, quadrigram)

    # Count occurrences of common English letters
    for char in deciphered_text:
        if char in most_common_english_letters_primary:
            common_letter_matches += 2
        elif char in most_common_english_letters_secondary:
            common_letter_matches += 1

    # Sum up the scores for an overall "English-likeness" score
    total_score = (
            common_word_matches +
            common_bigram_matches +
            common_trigram_matches +
            common_quadrigram_matches +
            common_letter_matches
    )
    return total_score
