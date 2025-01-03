from infolingo.main import get_word_stats, tokenize_text, pick_vocab


def test_tokenize_text(sample_text):
    words = tokenize_text(sample_text)
    assert words == ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]


def test_get_word_stats(sample_text):
    words = tokenize_text(sample_text)
    word_counts, word_probs = get_word_stats(words)
    assert word_counts == {
        "the": 2,
        "quick": 1,
        "brown": 1,
        "fox": 1,
        "jumps": 1,
        "over": 1,
        "lazy": 1,
        "dog": 1
    }


def test_pick_vocab_simple():
    vocab = pick_vocab("hello hello hello", n=1)
    assert vocab[0] == "hello"

def test_pick_vocab_simple2(sample_text):
    vocab = pick_vocab(sample_text, n=2)
    assert vocab[0] == "jumps"