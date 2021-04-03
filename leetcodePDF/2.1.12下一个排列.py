def reverse(p, i, j):
	j -= 1
	while i < j:
		p[i], p[j] = p[j], p[i]
		i += 1
		j -= 1
	return p

def solution(p):
	i = len(p) - 1
	while i > 0:
		if p[i-1] < p[i]:
			# do something
			p[i-1], p[i] = p[i], p[i-1]
			reverse(p, i+1, len(p)) # [i+1, len(p))
			j = i + 1
			t = p[i]
			while j < len(p) and p[j] < t:
				p[j-1] = p[j]
				j += 1
			p[j-1] = t
			return p
		else:
			i -= 1

	reverse(p, 0, len(p))
	return p
if __name__ == '__main__':
	# p = [1, 3, 4, 2]
	# print(solution(p))
	ps = [[1, 3, 4, 2], [3, 2, 1], [1, 1, 5], [1, 5, 1]]
	for p in ps:
		print([i for i in p], " solutions: ", solution(p))