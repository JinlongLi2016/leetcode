```
NewIt 
for it in intervals:
	if it.end < NewIt.start:
		continue
	elif it.start > NewIt.end: # 当前间隔的左端点大于 新间隔的右端点（无相交区域，可以直接插入。）
		# 在it前面插入NewIt
		intervals.insert(it, NewIt)
		return intervals
	else:
		NewIt.start = min(NewIt.start, it.start)
		NewIt.end = max(NewIt.end, it.end)
		intervals.erase(NewIt)

intervals.append(NewIt)
return intervals

```

intervals = []
for i, interval in enumerate(intervals):
	if interval.end < new.start:
		continue
	elif interval.start > new.end:
		interval.insert(i, new)
		return intervals
	else:
		new.start = min(new.start, interval.start)
		new.end = max(new.end, interval.end)
		intervals.pop(i)
intervals.append(new)
return intervals