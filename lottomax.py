import random
from os import pipe

def get_numbers():

    lomax_num = range(1, 50)
    r_round = range(1, 445)
    isFirst = False

    lomax_arr = []

    for r in r_round :
        if r == 444 :
            print(f'Round is {r}')
            while 8 > len(lomax_arr) :
                pick = random.randint(1, 50)

                if isFirst == False :
                    print(f'First number is : {pick}')
                    lomax_arr.append(pick)
                    isFirst = True
                else :
                    found = False

                    for picked in lomax_arr :
                        if found == False:
                            # print(f'{picked} : {pick}')
                            if picked != pick :
                                lomax_arr.append(pick)
                                # print(lomax_arr)
                                if len(lomax_arr) == 2 :
                                    print(f'Sencond number is : {pick}')
                                    found = True
                                if len(lomax_arr) == 3 :
                                    print(f'Third number is : {pick}')
                                    found = True
                                if len(lomax_arr) == 4 :
                                    print(f'Forth number is : {pick}')
                                    found = True
                                if len(lomax_arr) == 5 :
                                    print(f'Fifth number is : {pick}')
                                    found = True
                                if len(lomax_arr) == 6:
                                    print(f'Sixth number is : {pick}')
                                    found = True
                                if len(lomax_arr) == 7:
                                    print(f'Seventh number is : {pick}')
                                    found = True
                        break
    lomax_arr.sort()
    print(lomax_arr)

get_numbers()
