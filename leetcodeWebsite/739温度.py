
def temperature(T: list):
    S, res = [], []
    n = len(T)
    for idx in range(n)[::-1]:
        if len(S) > 0 and T[idx] >= T[S[-1]]:
            while len(S) > 0 and T[idx] >= T[S[-1]]:
                S.pop()
            right_index = idx if len(S) == 0 else S[-1]
            res.append(right_index - idx)
        else:
        	# 若为空，表明右侧无比idx更高的元素；否则最后的元素在栈顶处
        	res.append(0 if len(S) == 0 else S[-1] - idx)
        S.append(idx)
    return res[::-1]



def temperature_clean(T: list):
    S, res = [], []
    n = len(T)
    for idx in range(n)[::-1]:
        if len(S) > 0 and T[idx] >= T[S[-1]]:
            while len(S) > 0 and T[idx] >= T[S[-1]]:
                S.pop()
        right_index = idx if len(S) == 0 else S[-1]
        res.append(right_index - idx)
        S.append(idx)
    return res[::-1]

if __name__ == '__main__':
	t = []
	print(temperature(t))