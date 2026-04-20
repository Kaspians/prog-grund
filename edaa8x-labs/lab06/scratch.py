import os


# NOTE: copy of ./words.py
def read_words(filename, print_words):
    # se till att vi öppnar filen i rätt katalog (slå samman katalogen som scriptet ligger i med filnamnet på textfilen)
    filepath = os.path.join(
        os.path.dirname(__file__), filename
    )  # INFO: gets directory-name of the current file, and merge it with specified filename

    # öppna filen (utf-8 behövs för att hantera åäö rätt)
    file = open(filepath, encoding='utf-8')

    if print_words == 'y':  # NOTE: added only if y
        for line in file:
            print(line)

    def count_only(words, count_words):
        # ännu ej implementerad
        pass

    def count_all_except(words, stopwords):
        # ännu ej implementerad
        pass

    def filter_hist(hist, min_count):
        # ännu ej implementerad
        pass

    def sorted_hist(hist):
        # ännu ej implementerad
        pass


# -----------------------------------------------------------
# namnet på filen som ska läsas
filename = 'nilsholg.txt'
answer = input('press [y] to print words: ')
read_words(filename, answer)

###############
## UPPGIFTER ##
###############
#
# 1. Intro
# 2.
# 3.
# 4.
# 5.
