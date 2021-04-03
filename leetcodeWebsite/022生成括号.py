# 022 

def forward(i, j, n, tmpList, res):
    if j == n:
        res.append("".join(tmpList))
        return
    else:
        if i == j:
            tmpList.append('(')
            forward(i+1, j, n, tmpList, res)
            tmpList.pop()
        else:
            if i < n:
                tmpList.append('(')
                forward(i+1, j, n, tmpList, res)
                tmpList.pop()
            tmpList.append(')')
            forward(i, j+1, n, tmpList, res)
            tmpList.pop()
        
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        forward(0, 0, n, [], res)
        return res
        
        
# https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python

def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))