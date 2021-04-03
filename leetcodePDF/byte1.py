a = input().strip()
n = int(a)
lst = input().strip()
lst = [int(i) for i in lst.split(' ')]
seenlst = [0] * n

st = [max(lst) + 1]

for i in range(n-1, -1, -1):
    if lst[i] < st[-1]:
        st.append(lst[i])
    elif lst[i] > st[-1]:
        while lst[i] > st[-1]:
            st.pop()
            seenlst[i] += 1
        st.append(lst[i])

print(lst[seenlst.index(max(seenlst))])