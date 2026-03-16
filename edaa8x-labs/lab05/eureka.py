#!/bin/python3
# Never goon

from eureka_assets import fn


def main():
    ask = fn.asking()  # who axed?
    while ask:  # as long axing ain't make no ask empty
        if ask == "add":  # TODO: allow to write 'add "foobar"' (etc) directly
            fn.add()
        elif ask == "del":  # TODO: allow multiple deletes
            fn.ls()
            fn.delete()
        elif ask == "ls":
            fn.ls()
        elif ask == "help":
            fn.help()
        else:
            print("\nWTF is dis?", ask)

        ask = fn.asking()  # I did the axing

    fn.debugger()  # to (de)bug, or not to (de)bug


main()
