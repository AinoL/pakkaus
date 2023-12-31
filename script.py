from enum import Enum
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

class Destination(Enum):
    city = 1
    climbing = 2
    camping = 3
    kayaking = 4
    cabin = 5

def gear(i):
    with open("lists/" + Destination(int(i)).name + ".txt") as f:
        lines = f.readlines()
    return list(map(lambda x: x.replace("\n", ""), lines))

def multipliers(nights, final_set):
    for g in final_set:
        if g in multiplier_dict:
            final_set.add(g + ' * ' + str(math.ceil(multiplier_dict[g] * nights)))
            final_set.remove(g)
    return final_set

def concatlist():
    for d in Destination:
        print('{:15} = {}'.format(d.name, d.value))
    

def main():
    concatlist()
    destination_input = input ('Where are you going? Give list as numbers like \'13\': ')
    try:
        final_gear = []
        val = int(destination_input)
        for i in str(val):
            final_gear += gear(i)
        final_set = set(final_gear)
    except ValueError:
        print("That's not an number!")

    night_input = input ('How many nights?: ')
    try:
        val = int(night_input)
        final_set = multipliers(val, final_set)
        print(list(final_set))
    except ValueError:
        print("That's not an number!")

if __name__ == "__main__":
    main()
