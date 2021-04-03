class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # find a zero
        ti, tj = None, None
        for i in range(len(matrix)):
        	for j in range(len(matrix[0])):
        		if matrix[i][j] == 0:
        			ti, tj = i, j
        			break
        if ti is None:
        	return None

        for i in range(len(matrix)):
        	for j in range(len(matrix[0])):
        		if matrix[i][j] == 0:
        			matrix[ti][j] = 0
        			matrix[i][tj] = 0 
        for i in range(len(matrix)):
        	if i != ti and matrix[i][tj] == 0:
        		for j in range(len(matrix[0])):
        			matrix[i][j] = 0
        for j in range(len(matrix[0])):
        	if j != tj and matrix[ti][j] == 0:
        		for i in range(len(matrix)):
        			matrix[i][j] = 0
