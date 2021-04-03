
def divide2(dividend, divisor):
	r = 0
	while dividend >= divisor:
		c = divisor

		# 把 c 每次增加一倍
		i = 0
		while dividend >= c:
			dividend -= c 
			r += 1 << i 
			c = c << 1

			i += 1
	print(r)

divide2(25, 25)