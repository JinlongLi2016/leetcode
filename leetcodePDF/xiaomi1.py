lst = input().strip()
lst = [int(i) for i in lst.split(' ')]
r = [0] * len(lst)

r[0] = lst[0]
for i in range(1, len(lst)):
    r[i] = lst[i] + r[i-1] if r[i-1] > 0 else lst[i]

print(max(r))

