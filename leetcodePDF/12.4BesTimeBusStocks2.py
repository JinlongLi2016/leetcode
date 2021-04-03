
p = []

def maxprice(p):
	# as solution gives, sum all partitions' gain.
	if len(p) < 2:
		return 0

	min_price = p[0]

	total_gain = 0
	tmp_gain = 0

	i = 1
	while i < len(p):
		if p[i] < min_price:
			min_price = p[i]
			total_gain += tmp_gain
		else:
			tmp_gain = max(tmp_gain, p[i] - min_price)
		i += 1
