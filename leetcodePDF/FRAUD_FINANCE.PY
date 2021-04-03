from functools import reduce

def f(x):
	l = [1./((1+x)**(i)) for i in range(12)]
	return 226.61 * sum(l) 


# def bs(l, r, t):
# 	mid = (l+r)/2
# 	middle = f(mid)
# 	while abs(middle - t) > 1e-2:
# 		# print(abs(middle - t))
# 		if(middle < t):
# 			r = mid
# 		else:
# 			l = mid
# 		mid = (l+r)/2.
# 		middle = f(mid)
# 	print(f(mid))
# 	return mid

def bs(l, r, t):
	while abs(l - r) > 1e-6:
		mid = (l + r) / 2
		middle = f(mid)
		if (f(r) - t) * (middle - t) > 0:
			r = mid 
		else: 
			l = mid 
	print('mid', mid, 'f(mid)', f(mid))
	return mid # month rate


# t = 0.029
# print(f(t))
# print(bs(0, 1,120) * 12)
# print('rate:', t*12)

r = bs(0, 1, 2518)
print('year rate: {0:.2%}'.format(r*12))
