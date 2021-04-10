def forward(cands, idx, d, s, t, p, res):
    if s == t:
        res.append(p[:])
    elif s > t or idx >= len(cands):
        return
    else:
        v = d[cands[idx]]

        for i in range(v + 1):
            if s + cands[idx] * i > t:
                break
            d[cands[idx]] -= i
            forward(cands, idx + 1, d, s + cands[idx] * i, t, p + [cands[idx]] * i, res)
            d[cands[idx]] += i

class Solution:
    def combinationSum2(self, candidates, target):
        # converting into defaultdict
        d = {}
        for c in candidates:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = []
        cands = list(set(d.keys()))
        forward(cands, 0, d, 0, target, [], res)
        return res


if __name__=="__main__":
    s = Solution()
    # print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([1,2,1,1], 3))