from task_word_rank import display_counted_words, find_total_n_words
import inspect

"""
UNIT TESTS
"""


def test_find_total_n_words():
    """
    GIVEN
    sentence with multiple reapeted words
    """
    sentence = [
        'mam',
        'mam ala kota i jeszcze jednego kota',
        'mam ala'
    ]

    """
    WHEN
    use function that calculate total number of word
    """
    result = find_total_n_words(sentence, 3)

    """
    THEN
    Returned tuples with correct number for each word that are repeated
    """
    expected_result = [('mam', 3), ('ala', 2), ('kota', 2)]
    assert result == expected_result


def test_count_for_first_1_words():
    """
    GIVEN
    array of sentences
    """
    total_words = [
        ('mam', 4)
    ]

    """
    WHEN
    use function to display total words
    """
    result = display_counted_words(total_words)

    """
    THEN
    user can see corrent number for one word
    """
    assert result == "'mam' = 4"


"""
FUNCTIONAL tests
"""


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
