# 135 Candy 糖果

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return *the minimum number of candies you need to have to distribute the candies to the children*.



* mine

```python
def des_list(ratings): # 每一个位置存储该位置向右连续下降序列的长度
    des = [ratings[i] > ratings[i+1] for i in range(len(ratings) - 1)] + [0]
    des = des[::-1]
    acc = 0
    for idx, d in enumerate(des):
        if d:
            acc += 1
        else:
            acc = 0
        des[idx] = acc
    return des[::-1]
class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = des_list(ratings)
        r2l = des_list(ratings[::-1])[::-1]
        ass = [0] * len(ratings)
        for idx, r in enumerate(ratings):
            ass[idx] = max(l2r[idx], r2l[idx]) + 1
        return sum(ass)
```

* M2

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        assigns = [1] * n
        for i in range(1, n): # 从左到右边
            if ratings[i] > ratings[i-1]:
                assigns[i] = assigns[i-1] + 1
        for i in range(n-2, -1, -1): # 从右到左
            if ratings[i] > ratings[i+1]:
                assigns[i] = max(assigns[i], assigns[i+1] + 1)
        return sum(assigns)
```

