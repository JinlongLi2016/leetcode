#coding:utf-8
import sys
print(sys.version)
prices_sequence = [0, 1, 2, 3, 4, -5, -6, 8, -2]

def profit(prices_sequence):
	if len(prices_sequence)<2:
		return 0
	# 边界条件判断错误
	# if len(prices_sequence)<=2:
	# 	d = prices_sequence[1] - prices_sequence[0]
	# 	return d if d > 0 else 0

	d = 0
	min_price = prices_sequence[0]
	i = 1

	while i < len(prices_sequence):
		if prices_sequence[i] < min_price:
			min_price = prices_sequence[i]
		else:
			d = max(d, prices_sequence[i] - min_price)
		i += 1

	return d

print(profit(prices_sequence))