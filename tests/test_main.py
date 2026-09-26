from main import count_words


def test_counts_words_and_uniques():
    assert count_words("a b a") == {"words": 3, "unique": 2}


def test_empty_string():
    assert count_words("") == {"words": 0, "unique": 0}
