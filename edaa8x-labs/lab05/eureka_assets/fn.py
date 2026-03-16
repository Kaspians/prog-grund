def file_path(file):
    path = (  # INFO: delar upp path och skapar lista av items mellan '/'(utan den sista item[-1]). sen join till en string med '/' imellan och append '/eureka.txt'
        "/".join(__file__.split("/")[0:-1]) + f"/{file}"
    )  # kan istället använda `rsplit`...
    return path


def read_file(file):
    # print("\nReading file", file_path(file))
    n = 0
    with open(file_path(file), "r") as f:
        for line in f:
            print(f"{n} {line.strip()}")
            n += 1
    print()


def append_file(file, item):
    # print("\nWriting to file", file_path(file))
    with open(file_path(file), "a") as f:  # a = append
        f.write(item)


def write_file(file, item):
    # print("\nWriting to file", file_path(file))
    with open(file_path(file), "w") as f:  # a = append
        f.write(item)


#############
## ACTIONS ##
#############


def asking():
    return input("What u wanna do?\n[add]/[del]/[ls]/[help]/[<enter>]: ")


def add():
    append_file("eureka.txt", f"\n{input("Eureka? ")}")
    debug_add("eureka.txt written")


def ls():
    read_file("eureka.txt")


def delete():  # TODO: delete {n}item in eureka.txt
    line = int(input("Which line to delete? "))
    eureka_lines = []
    file = "eureka.txt"
    with open(file_path(file), "r") as f:
        for i in f:
            eureka_lines.append(i)

    debug_add(f"del - eureka_lines list created")

    del eureka_lines[line]
    debug_add(f"del - item {line} in eureka_lines deleted")

    write_file(file, "")
    debug_add(f"del - rewrote/cleared eureka.txt")

    for i in eureka_lines:
        append_file(file, i)
    debug_add(f"del - re-added all items except the deleted line: {line}")


def help():  # TODO: print from a file
    print("""
    ############
    ## HELP!! ##
    ############
    """)
    read_file("help.md")
    debug_add("Asked for help... lol?")


###########
## DEBUG ##
###########

DEBUG = []
log_file = "log.log"


def debug_add(item):  # add items to debug-list
    DEBUG.append(item)


def debugger():
    write_file(log_file, "log.log rewritten")  # rewrites the log-file
    for i in DEBUG:
        append_file(log_file, f"\n{i}")  # append Debug items to log-file
    debug_tf = input("Print debug? [y/N] ")  # True/False to show DEBUG
    # debug_tf = False # hardcodes
    if debug_tf == "y":
        print("""
    ##################
    ## EUREKA DEBUG ##
    ##################
    """)
        read_file(log_file)
