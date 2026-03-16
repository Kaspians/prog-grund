#!/bin/python3
# Never goon

import fn

EUREKAS = []


def eureka_add():
    fn.add_list(EUREKAS, input("Eureka? "))
    fn.debug_add("EUREKA added")


def eureka_write():
    fn.write_file(input("Eureka? "))
    fn.debug_add("EUREKA written")


def main():
    asking = fn.ask()
    while asking:
        if asking == "add":
            eureka_add()
        elif asking == "write":  # TODO: make this 'add'
            eureka_write()
        elif asking == "del":
            fn.delete()
        elif asking == "ls":
            fn.print_items(EUREKAS)
        elif asking == "read":  # TODO: make this 'ls'
            fn.read_file()
        elif asking == "help":
            fn.help()
        else:
            print("wtf is dis?", asking)
        asking = fn.ask()

    # debug_tf = input("Print debug? (empty=False) ")  # True/False to show DEBUG
    debug_tf = False
    if debug_tf:  # HACK: hardcoded
        fn.print_debug()


main()
