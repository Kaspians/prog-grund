from pathlib import Path
import file_reader

### 9
import weather_functions as wf

### 12
from weather_functions import calculate_avg_temp as wfcalc
from weather_functions import when_is_spring as wis
from weather_functions import when_is_spring2 as wis2

# from weather_functions import main

# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / "temperatur_data.csv"

# read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 2)

###########################################################

#########
### 1 ###
#########
# print("\n1")
# läs?
#########
### 2 ###
#########
# print("\n2")

# Läser varje rad i filen.csv och för varje rad som vars månad matchar något
#   skriver in datan i tmpfile


#########
### 3 ###
#########
# print("\n3")
# ok?
#########
### 4 ###
#########
# print("\n4")
#
# avg_temp = sum(temp_list) / len(temp_list)
#
# # print(avg_temp)
# print(format(avg_temp, ".2f"))  # NOTE: behövs ej här; men dock senare

#########
### 5 ###
#########
# print("\n5")


# def calculate_avg_temp(l):
#     sm = 0
#     n = 0
#     for i in l:
#         sm += i
#         n += 1
#     return sm / n


# print("sm", sm)
# print("n", n)

#########
### 6 ###
#########
# print("\n6")

# avg_temp2 = calculate_avg_temp(temp_list)
# print("avg_temp2 =", format(avg_temp2, ".2f"))  # NOTE: btw, format() behövs

#########
### 7 ###
#########
# print("\n7")
# print("Ok, försökte fundera... ehm?")

#########
### 8 ###
#########
# print("\n8")

# Kör filen? BUG: BRICK

#########
### 9 ###
#########
# print("\n9")
#
# # pallar ej skriva weather_functions
# avg_temp2 = wf.calculate_avg_temp(temp_list)
# print("avg_temp2 =", format(avg_temp2, ".2f"))  # NOTE: btw, format() behövs

##########
### 10 ###
##########
# print("\n10")
# ok
##########
### 11 ###
##########
# print("\n11")
# great, har gjort det redan
##########
### 12 ###
##########
# print("\n12")
#
#
# avg_temp3 = wfcalc(temp_list)
# print("avg_temp3 =", format(avg_temp2, ".2f"))  # NOTE: btw, format() behövs

##########
### 13 ###
##########
# print("\n13")
# when_spring = wis(temp_list)
# when_spring = wis(temp_list_year)
# when_spring = wis(temp_list_n)
# print(when_spring)

##########
### 16 ###
##########
print("\n16")


def main(val):
    if val == 1:
        m = int(
            input(
                "Vilken månad vill du beräkna medeltemperatur för? Ange månadsnummer\n"
            )
        )
        temp_list_n = file_reader.read_from_file(file_path, m)
        print(
            "Medeltemperaturen var",
            format(wfcalc(temp_list_n), ".2f"),
            "grader i månad",
        )
    elif val == 2:
        # vanilla
        temp_list_year = file_reader.read_from_file(file_path, 0)
        print("Letar efter våren...")
        print("Vår kommer för [månad, dag]", wis(temp_list_year))
        ### 20
        # efter = int(input("Från vilken dag börja räkna? 0 för att igga\n"))
        # temp_list_year = file_reader.read_from_file(file_path, 0, efter)
        # print("Letar efter våren...")
        # print("Vår kommer för [månad, dag]", wis2(temp_list_year))
    ### 18
    elif val == 3:
        print("\nupg 18")
        m = int(input("Vilken månad vill du ha min och max?\n"))
        temp_list_n = file_reader.read_from_file(file_path, m)
        print("max", max(temp_list_n))
        print("min", min(temp_list_n))
    else:
        print("Fel number")


print(
    "Vad vill du göra? Tryck 1 för medeltemperatur\n",
    "2 för vårens ankomst\n",
    "3 för min och max",
)
val = int(input())
main(val)


# print("extra uppgifter")

##########
### 18 ###
##########


################
## scratchpad ##
################

# TEST:
# print(f"\n\ntemp_list = {temp_list}")
# print(f"\n\ntemp_list_year = {temp_list_year}")
