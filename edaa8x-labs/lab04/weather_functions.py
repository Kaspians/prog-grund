#!/usr/bin/python3


#########
### 8 ###
#########


def calculate_avg_temp(l):
    sm = 0
    n = 0
    for i in l:
        sm += i
        n += 1
    return sm / n


# Kör filen? Inget händer

##########
### 13 ###
##########


def when_is_spring(temp_list):
    c = 0  # dagar i sträck counter
    n = 45  # dag n
    # print(temp_list)  # TEST: print data listen
    while c < 7:
        if temp_list[n] > 0.0:
            c += 1
        else:
            c = 0
            print(f"day {n+1} do be cold")
        n += 1
    mon31 = [0, 2, 4, 6, 7, 9, 11]
    mon30 = [3, 5, 8, 10]
    months = list(range(12))
    for i in months:
        if i in mon31:
            months[i] = 31
        elif i in mon30:
            months[i] = 30
    months[1] = 28
    ni = 0
    nm = 0
    while n > months[ni]:
        n -= months[ni]
        nm += months[ni]
        ni += 1
    nr = [nm, n]
    # print("c", c)
    if c >= 7:
        return nr
    else:
        return -1
    # NOTE: ? igentligen n 1 för stor, men det är dag n+1 innan det, så jämnar ut


#### 20
def when_is_spring2(temp_list):
    c = 0  # dagar i sträck counter
    n = 0  # dag n
    # print(temp_list)  # TEST: print data listen
    for i in temp_list:
        if c < 7:
            if temp_list[n] > 0.0:
                c += 1
            else:
                c = 0
                print(f"day {n+1} do be cold")
        n += 1
    mon31 = [0, 2, 4, 6, 7, 9, 11]
    mon30 = [3, 5, 8, 10]
    months = list(range(12))
    for i in months:
        if i in mon31:
            months[i] = 31
        elif i in mon30:
            months[i] = 30
    months[1] = 28
    ni = 0
    nm = 0
    while n > months[ni]:
        n -= months[ni]
        nm += months[ni]
        ni += 1
    nr = [nm, n]
    # print("c", c)
    if c >= 7:
        return nr
    else:
        return -1
    # NOTE: ? igentligen n 1 för stor, men det är dag n+1 innan det, så jämnar ut
