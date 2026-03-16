#!/bin/python3
# Never goon

DEBUG = []
EUREKAS = []


def add_list(list, item):  # add item to list
    list.append(item)


def new_eureka(eureka):
    add_list(EUREKAS, eureka)


def print_items(list):
    n = 0
    for i in list:  # properly formats each string-item
        print(n, i)
        n += 1


def main():
    while_on = ""
    while not while_on:  # change to option = repeat ; nothing = end
        new_eureka(input("Eureka? "))
        while_on = input("Stop? Any button and enter to stop: ")
        add_list(DEBUG, "added")

    print_items(EUREKAS)

    # debug_tf = input("Print debug? (empty=False) ")  # True/False to show DEBUG
    if True:  # HACK: hardcoded
        print("""
##################
## EUREKA DEBUG ##
##################""")
        print_items(DEBUG)  # Kanske skapa LOG istället


main()
