DEBUG = []


def add_list(list, item):  # add item to list
    list.append(item)


def debug_add(item):  # TODO: add to file instead
    add_list(DEBUG, item)


def print_items(list):
    n = 0
    for i in list:  # properly formats each string-item
        print(n, i)
        n += 1


def print_debug():
    print("""
##################
## EUREKA DEBUG ##
##################""")
    print_items(DEBUG)  # Kanske skapa LOG istället


file = "eureka.txt"  # Hard coded
file_path = (  # INFO: delar upp path och skapar lista av items mellan '/'(utan den sista item[-1]). sen join till en string med '/' imellan och append '/eureka.txt'
    "/".join(__file__.split("/")[0:-1]) + f"/{file}"
)  # kan istället använda rsplit...


def read_file():
    print("\nreading file", file_path)
    with open(file_path, "r") as f:
        for line in f:
            print(line.strip())


def write_file(item):
    print("\nwriting to file", file_path)
    with open(file_path, "a") as f:  # a = append
        f.write(item)


def ask():
    return input("What u wanna do?\n[add]/[del]/[ls]/[help]/[<enter>]: ")


def delete():  # TODO: print a {n} in EUREKAS
    print()
    debug_add("eureka deleted")


def help():  # TODO: print from a file
    print("idk, figure it out...")
    debug_add("Asked for help... lol?")
