# Author: EBP (AMDG) 12/10/20

def sums(a):
    f = 0
    for x in a:
        if x % 2 == 0:
            f += x
        else:
            if x % 2 != 0:
                del a[:x]
    return f


print(sums([2, 4, 6, 8, 9]) == 20)
print(sums([13, 12, 10]) == 0)
print(sums([14, 16, 32]) == 62)