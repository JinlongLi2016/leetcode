n, m = [int(i) for i in input().strip().split(' ')]

A = [int(i) for i in input().strip().split(' ')]
B = [int(i) for i in input().strip().split(' ')]


def max2_func(lst):
    max1, max2 = lst[0], lst[1]
    max1, max2 = (max2, max1) if max1 > max2 else (max1, max2)
    for i in range(2, len(lst)):
        if lst[i] >= max2:
            max2, max1 = lst[i], max2
        elif lst[i] >= max1:
            max1 = lst[i]
    return [max1, max2 ]

def min2_func(lst):
    lst = [-i for i in lst]
    max1, max2 = lst[0], lst[1]
    max1, max2 = (max2, max1) if max1 > max2 else (max1, max2)
    for i in range(2, len(lst)):
        if lst[i] >= max2:
            max2, max1 = lst[i], max2
        elif lst[i] >= max1:
            max1 = lst[i]
    return [-max1, -max2 ]


mA = max2_func(A) + min2_func(A)
mB = max2_func(B) + min2_func(B)


r = []
for i in mA:
    for j in mB:
        r.append(i * j)
r.sort()
print(r[-2])