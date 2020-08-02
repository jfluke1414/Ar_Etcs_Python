import random
from os import pipe

def get_numbers():
    isFirst = False
    lomax_arr = []
    same_arr = []
    while 7 > len(lomax_arr):
        pick = random.randint(1, 50)

        if isFirst == False:
            print(f'First number is : {pick}')
            lomax_arr.append(pick)
            isFirst = True
            i = 1
        else:
            for picks in lomax_arr:
                if picks == pick:
                    # found = True
                    same_arr.append(pick)
                    print(f'same_arr : {same_arr}')

            if len(same_arr) == 0:
                lomax_arr.append(pick)
            else:
                for same_picks in same_arr:
                    if same_picks != pick:
                        lomax_arr.append(pick)
            if len(lomax_arr) == 2:
                print(f'Sencond number picked is : {pick}')
            if len(lomax_arr) == 3:
                print(f'Third number picked is : {pick}')
            if len(lomax_arr) == 4:
                print(f'Forth number picked is : {pick}')
            if len(lomax_arr) == 5:
                print(f'Fifth number picked is : {pick}')
            if len(lomax_arr) == 6:
                print(f'Sixth number picked is : {pick}')
            if len(lomax_arr) == 7:
                print(f'Seventh number picked is : {pick}')
    print(f'lomax_arr : {lomax_arr}')
    lomax_arr.sort()

def get_round():
    r_round = range(1, 445)
    for r in r_round :
        if r == 444 :
            print(f'Round is {r}')
            get_numbers()

get_round()