# Author: EBP (AMDG) 12/10/20

def sum_odds(my_list):
    x = 0
    for odds in my_list:
        if odds % 2 != 0:
            x += odds
    return x

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)
