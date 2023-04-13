from task_word_rank import display_counted_words, find_total_n_words
import inspect


def test_count_for_first_1_words():
    sentence = [
        'mam',
        'mam mam',
        'mam'
    ]

    total_words = find_total_n_words(sentence, 1)
    result = display_counted_words(total_words)
    assert result == "'mam' = 4"


def test_count_top_first_3_words():

    """
    GIVEN
    ***input:*** array with multiple strings\
    """
    sentence = [
        'mam',
        'mam ala kota i jeszcze jednego kota',
        'mam ala'
    ]

    """
    When
    """
    total_words = find_total_n_words(sentence, 3)
    result = display_counted_words(total_words)

    """
    THEN
    ***expected output:***
    rank of the 3 most often repeated words in given
    set of strings and number of times they occured,
    case insensitive
    """
    # cleandoc is used to maintain relative intendantion in multiline string
    expected_text = inspect.cleandoc("""
        'mam' = 3
        'ala' = 2
        'kota' = 2""")

    assert result == expected_text
