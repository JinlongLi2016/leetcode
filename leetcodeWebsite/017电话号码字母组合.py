17. Letter Combinations of a Phone Number

d = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

def forward(s, i, prevstr, res):
    if len(s) == i:
        res.append(prevstr)
    else:
        for t in d[int(s[i])]:
            forward(s, i+1, prevstr + t, res)
            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        forward(digits, 0, '', res)
        return res
        
#### Solution 2: 使用 yield 

def forward(s, i, prevstr):
    if len(s) == i:
        yield prevstr
    else:
        for t in d[int(s[i])]:
            for p in forward(s, i+1, prevstr + t):
                yield p
            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return list(forward(digits, 0, ''))
        
        
### A solution from forums 
def letterCombinations(self, digits):
    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
    cmb = [''] if digits else []
    for d in digits:
        cmb = [p + q for p in cmb for q in dict[d]]
    return cmb