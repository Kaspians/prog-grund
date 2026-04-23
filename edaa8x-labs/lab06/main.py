#!/usr/bin/env python3

from sys import stdout
import words as fn


def print2(t: tuple) -> None:
    for i in t:
        stdout.write(i + '\t')
    stdout.write('\n')


print2(('Lab06', 'Interactive session'))


def main(filename: str, countOnlyFile: str, stopWordsFile: str, choice: int) -> None:
    """
    First para is the base file of words, second is words for count only
    function, third is for count NOT function.

    With input() select the function you want to do.
    * See `ask()`
    """
    words = fn.read_words(filename)
    provinces = fn.read_words(countOnlyFile)
    stopwords = fn.read_words(stopWordsFile)

    def sep() -> None:
        print('--------------------------------------------------------')

    wordsProv = fn.count_only(words, provinces)
    wordsStop = fn.count_all_except(words, stopwords)

    # print(wordsStop['gåskarlen'])

    sep()
    if choice == 0:
        print(words)
    elif choice == 1:
        print('First 100:\n', words[:100])
        sep()
        print('Last 100:\n', words[-100:])
    elif choice == 2:
        print(wordsProv)
    elif choice == 3:
        for t in fn.sorted_hist(wordsStop)[-10:]:
            print(t, t[0], t[1])
    elif choice == 4:
        filterDic = fn.filter_hist(
            fn.count_all_except(words, []), 100
        )  # count all words except nil
        n = 0
        for i in fn.sorted_hist(filterDic):
            print(i)
            n += 1
        print(f'nr of words that appear 100+ times: {n}')
    else:
        print('What?')
    sep()


filename = 'nilsholg.txt'
countOnlyFile = 'landskap.txt'
stopWordsFile = 'undantagsord.txt'


def ask():
    """
    With input() select the function you want to do.
    * 0. Print(all words)
    * 1. Print(first/last 100 cleaned words)
    * 2. Print(Count only provinces)
    * 3. Print(Top 10 of all except stopwords)
    * 4. Print(Filter away words rarer than `n` appearances)
    """
    stdout.write("""
    Choose the option you want {int}:
    * 0. Print(all words)
    * 1. Print(first/last 100 cleaned words)
    * 2. Print(Count only provinces)
    * 3. Print(Top 10 of all except stopwords)
    * 4. Print(Filter away words rarer than {n} appearances)
    """)
    return input('Choice: ')


while True:
    choice = ask()
    if choice == '':
        break
    elif int(choice) > 4 or int(choice) < 0:
        stdout.write('0<=Int<5, thanks\n')
    else:
        main(filename, countOnlyFile, stopWordsFile, int(choice))
