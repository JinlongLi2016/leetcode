def processLine(line, wordlen, maxWidth, isLastLine=False):
    if len(line) == 1:
        return line[0] + ' ' * (maxWidth - wordlen)
    if isLastLine:
        return ' '.join(line) + ' ' * (maxWidth - wordlen - (len(line) - 1))
    emptySpaceNum = maxWidth - wordlen
    baseEmp = emptySpaceNum // (len(line) - 1)
    extraEmp = emptySpaceNum % (len(line) - 1)
    t = line[0]
    i = 0
    while i < len(line) - 1:
        if i < extraEmp:
            t += ' ' * baseEmp + ' ' + line[i + 1]
        else:
            t += ' ' * baseEmp + line[i + 1]
        i += 1
    return t


class Solution:
    def fullJustify(self, words, maxWidth: int):
        line = []
        wordlen = 0
        res = []
        for word in words:
            if wordlen == 0:
                line.append(word)
                wordlen = len(word)
            else:
                if maxWidth - (wordlen + len(line) - 1) >= len(word) + 1:
                    line.append(word)
                    wordlen += len(word)
                else:
                    res.append(processLine(line, wordlen, maxWidth))

                    line, wordlen = [word], len(word)
        if line:
            res.append(processLine(line, wordlen, maxWidth, True))
        return res
s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."] ,16))