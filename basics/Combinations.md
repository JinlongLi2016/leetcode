## 组合

一个n个元素的数组，生成其所有的组合。

---

元素可能重复

```python
def combinations(cands):
    cands.sort()
    res = []
    dfs(cands, 0, [], res)
	return res

def dfs(cands, start, path, res):
    res.append(path[:])
    for i in range(start, len(cands)):
        if i == start or cands[i] != cands[i-1]:
            dfs(cands, i + 1, path + [cands[i]], res)

if __name__ == '__main__':
    print(combinations([1, 1, 3]))
```



