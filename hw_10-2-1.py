# Author: EBP (AMDG) 12/10/20

def count_odds(my_list):
    x = 0
    for i in my_list:
        if i % 2 != 0:
            x += 1
    return x

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 0)
print(count_odds([2, 4, 6, 8, 10]) == 5)

# I can't figure out how to make it spit out True for each statement only the first