def dfs(i, j, board, state, s):
    if len(s) == 0:
        return True
    if i > 0 and state[i - 1][j] == 0 and board[i - 1][j] == s[0]:
        state[i - 1][j] = 1
        if dfs(i - 1, j, board, state, s[1:]):
            return True
        else:
            state[i - 1][j] = 0
    if i < len(board) - 1 and state[i + 1][j] == 0 and board[i + 1][j] == s[0]:
        state[i + 1][j] = 1
        if dfs(i + 1, j, board, state, s[1:]):
            return True
        else:
            state[i + 1][j] = 0
    if j > 0 and state[i][j - 1] == 0 and board[i][j - 1] == s[0]:
        state[i][j - 1] = 1
        if dfs(i, j - 1, board, state, s[1:]):
            return True
        else:
            state[i][j - 1] = 0
    if j < len(board[0]) - 1 and state[i][j + 1] == 0 and board[i][j + 1] == s[0]:
        state[i][j + 1] = 1
        if dfs(i, j + 1, board, state, s[1:]):
            return True
        else:
            state[i][j + 1] = 0
    return False


class Solution:
    def exist(self, board, word: str) -> bool:
        state = []
        for _ in range(len(board)):
            state.append([0] * len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    state[i][j] = 1
                    if dfs(i, j, board, state, word[1:]):
                        return True
                    state[i][j] = 0
        return False
s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(s.exist(board, word))


