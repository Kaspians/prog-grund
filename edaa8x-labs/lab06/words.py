import string
import os


def read_words(filename: str) -> list[str]:
    """
    From file *'filename'* using relative path of the script, read each line.
    Then process each line into a *list* where:
    *   whitespace
    *   , . are stripped
    *   char made lawercase.

    Return a list of words
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # öppna filen (utf-8 behövs för att hantera åäö rätt)
    file = open(filepath, encoding='utf-8')

    listWords = []

    # skriv ut filens innehåll
    for line in file:
        lineWords = line.split()
        for word in lineWords:
            word2 = word.strip(string.punctuation + string.whitespace).lower()
            listWords.append(word2)

    return listWords


def count_only(words: list[str], count_words: list[str]) -> dict[str, int]:
    """
    Of the strings in **words**, only count **count_words**.

    Return a *keyVal* dict, where *key* is items in **count_words**,
    and *value* is how much they appeared in **words**.
    """
    keyVal = {k: 0 for k in count_words}
    for i in words:
        if i in count_words:
            keyVal[i] += 1
    return keyVal


def count_all_except(words: list[str], stopwords: list[str]) -> dict[str, int]:
    """
    Of the strings in **words**, count all except **stopwords**.

    Return a *keyVal* dict, of the counted strings.
    """
    keyVal = {k: 0 for k in words}
    for i in words:
        if i not in stopwords:
            keyVal[i] += 1
    return keyVal


def filter_hist(hist: dict[str, int], min_count: int) -> dict[str, int]:
    """
    Take a **dict** and integer **min_count**

    Return a dict where all *keys* with a *value* < *min_count*
    """
    newDic = {}
    for i in hist:
        if hist[i] > min_count:
            newDic[i] = hist[i]
    return newDic


def sorted_hist(hist: dict[str, int]) -> list[tuple[int, str]]:
    """
    Take a **dict**.

    Return a sorted version of *dict*.
    """
    lt = []  # lt = [l]ist of [t]uple
    for word in hist:
        lt.append((hist[word], word))
    lt.sort()
    return lt
