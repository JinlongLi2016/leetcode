from collections import namedtuple

# 对每个i采取


def maxpointsonaline(points):
	d = dict()

	n = len(points)
	result = 0
	for i in range(n):
		d.clear()
		samePoint = 0
		max_point = 1

		for j in range(i+1, n):
			if points[i].x == points[j].x:
				slope = float('+inf')
				if points[i].y == points[j].y:
					samePoint += 1
					continue
			else:
				slop = (points[j].y - points[i].y) / (points[j].x - points[i].x)
			cnt = 0
			if slop in d:
				d[slop] += 1
				cnt = d[slop]
			else:
				d[slop] = 2
				cnt = 2
			if max_point < cnt:
				max_point = cnt
		result = max(result, max_point + samePoint)
	print(result) 

point = namedtuple('points', ['x', 'y'])

xs = list(range(10))
xs[0], xs[5] = xs[5], xs[0]

ys = list(range(10, 20))
ys[0], ys[5] = ys[5], ys[0]

points = [point(i, j) for i, j in zip(xs, ys)]
maxpointsonaline(points)