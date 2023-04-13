from collections import defaultdict
from collections import Counter

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]


def find_total_n_words(sentences, n):
    '''
    sentences - array of sentences , each sentence is one element of array
    n - how many words to display starting from the most often
    '''

    word_set = set()
    counter = defaultdict(int)

    for line in sentences:
        word_list = line.split()
        for word in word_list:
            if word in word_list:
                word_set = word
                counter[word_set] += 1

    return Counter(counter).most_common(n)


def display_counted_words(words):
    text_result = []
    for word in words:
        text_result.append(f"'{word[0]}' = {word[1]}")
    result = '\n'.join(text_result)
    return result


result = find_total_n_words(sentences, 3)
print(display_counted_words(result))
