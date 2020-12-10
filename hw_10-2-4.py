# Author: EBP (AMDG) 12/10/20

def fname(a, b):
    x = 0
    for count in a:
        if b == count:
            x += 1
    return x


print(fname("cat", "t") == 1)
print(fname("apple", "p") == 2)
print(fname("supercalifragilisticexpialidocious", "i") == 7)