# main.py
import math
from collections import Counter
from typing import Tuple

from nltk import word_tokenize
from nltk.corpus import brown


########################
# VOCAB FUNCTIONS
########################
def get_word_stats(words: list[str]) -> Tuple[dict, dict]:
    """
    Get word count and word probability mass function (PMF) from list.
    :param words: list of words.
    :return: word counts and word PMF.
    """
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    word_probs = {word: count / total_words for word, count in word_counts.items()}
    return word_counts, word_probs


def tokenize_text(text: str) -> list[str]:
    """
    Tokenize text into words specific to a language, i.e. no
    numbers or special characters.
    :param text: input text.
    :return: list of words.
    """
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalnum()]
    words = [word for word in words if not word.isdigit()]
    return words


########################
# MAIN
########################
corpus = brown.words()
corpus_counts, corpus_probs = get_word_stats(corpus)


def pick_cross_entropy(
        words: list[str],
        corpus_word_probs: dict,
        n: int
):
    """
    Select the top n words that reduce cross-entropy the most.
    :param words: list of candidate words.
    :param corpus_word_probs: corpus word probabilities.
    :param n: number of words to select.
    :return: list of top n words using cross-entropy.
    """

    def _compute_entropy(w_counts, w_probs):
        entropy = 0
        for w in w_counts:
            entropy += math.log2(1 / corpus_word_probs.get(w, 0.00001)) * w_probs[w]
        return entropy

    # baseline entropy of text
    word_counts, word_probs = get_word_stats(words)
    baseline_entropy = _compute_entropy(word_counts, word_probs)
    deltas = []

    # remove each word in turn
    for word in word_counts:
        candidate_words = [w for w in words if w != word]
        candidate_word_counts, candidate_probs = get_word_stats(candidate_words)
        candidate_entropy = _compute_entropy(candidate_word_counts, candidate_probs)

        delta = baseline_entropy - candidate_entropy
        deltas.append((word, delta))

    # Pick the top words
    deltas = sorted(deltas, key=lambda x: x[1], reverse=True)
    picks = [w[0] for w in deltas[:n]]
    return picks


def pick_vocab(text: str, n: int) -> list[str]:
    """
    Select best vocabulary to learn from text.
    :param text: input text.
    :param n: number of words to select.
    :return: list of top n words to learn using cross-entropy.
    """
    words = tokenize_text(text)
    vocab = pick_cross_entropy(words, corpus_probs, n)
    return vocab
