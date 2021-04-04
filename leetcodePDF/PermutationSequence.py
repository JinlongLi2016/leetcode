def factorial(n):
	r = 1
	while n > 0:
		r = r * n
		n -= 1
	return r
def find_kth(n, k):
	k -= 1

	used = list(range(1, 1+n))
	lst = [None] * n

	while n > 0:
		r = k // factorial(n - 1)

		lst[n-1] = used[r]
		used.pop(r)

		k = k - r * factorial(n - 1)
		n -= 1

	return lst[::-1]
print(find_kth(3, 6))