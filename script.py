from enum import Enum
from aenum import MultiValueEnum
import math


final_set = {}
multiplier_dict = {
    "sukat": 1,
    "alushousut": 1,
    "aluspaidat": 1,
    "rintsikat": 0.3,
    "päällyspaidat": 0.3,
    "housut": 0.3
}

class Destination(MultiValueEnum):
    city = 1
    climbing = 2
    camping = 3
    kayaking = 4

def gear(i):
    with open("lists/" + Destination(int(i)).name + ".txt") as f:
        lines = f.readlines()
    return list(map(lambda x: x.replace("\n", ""), lines))

def multipliers(nights, final_set):
    multiplier_gear = []
    for g in final_set:
        if g in multiplier_dict:
            print(g + ' * ' + str(math.ceil(multiplier_dict[g] * nights)))

def main():
    destination_input = input ('Where are you going? \n 1 = city \n 2 = climbing \n 3 = camping \n 4 = kayaking \n Give list as numbers like \'13\': ')
    night_input = input ('How many nights?: ')
    try:
        final_gear = []
        val = int(destination_input)
        for i in str(val):
            final_gear += gear(i)
        final_set = set(final_gear)
    except ValueError:
        print("That's not an number!")
    try:
        val = int(night_input)
        multipliers(val, final_set)
    except ValueError:
        print("That's not an number!")

        

if __name__ == "__main__":
    main()
