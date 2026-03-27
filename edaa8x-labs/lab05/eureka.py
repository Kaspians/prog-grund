#!/bin/python3

from assets_eureka import fn


def main():
    ask = fn.asking()  # who axed?
    while ask:  # as long axing ain't make no ask empty
        if ask == 'add':
            fn.add('')
        elif ask == 'del':  # TODO: allow multiple deletes
            fn.ls()
            fn.delete()
        elif ask == 'ls':
            fn.ls()
        elif ask == 'help':
            fn.help()
        else:
            fn.else_what(ask)

        ask = fn.asking()  # I did the axing

    fn.debugger()  # to (de)bug, or not to (de)bug


main()

# TODO:
# Make `ask` instead be the first part of an array,
#   of which is the space-seperated array of user input.
#   (so i can use the rest of the array to use as arg if != empty)

##########
## KRAV ##
##########
#
# - [x] Min 2 func()            - 11/2
# - [x] Min 1 [list]            - 2/1 ? kanske way more
# - [x] Interact with user      - 
# - [x] Easy code to read and understand - check?
# - [x] keep it KISS stupid     - 😘
